from django.shortcuts import render
from .forms import UserInputForm
import qrcode
from io import BytesIO
from django.core.files import File
from .models import UserInput,HashedData
import base64
import hashlib

def hash_concat_strings(str1, str2):
    str1 = str1.upper().replace(" ", "")
    str2 = str2.upper().replace(" ", "")

    hash_str1 = hashlib.md5(str1.encode()).hexdigest()
    hash_str2 = hashlib.md5(str2.encode()).hexdigest()

    concatenated_hashes = hash_str1 + hash_str2

    final_hash = hashlib.md5(concatenated_hashes.encode()).hexdigest()

    return final_hash

def adjust_plate(plate):
    return plate.upper().replace(" ", "")

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer)
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

def input_form(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.save(commit=False)
            hashed_data = HashedData()
            data_to_encode = hash_concat_strings(user_input.field_one, user_input.field_two)
            if not HashedData.objects.filter(hashed_data=data_to_encode).exists():
                hashed_data.plate = adjust_plate(user_input.field_one)
                hashed_data.hashed_data = data_to_encode
                hashed_data.save()
            qr_code = generate_qr_code(data_to_encode)
            return render(request, 'result.html', {'qr_code': qr_code})
    else:
        form = UserInputForm()
    
    return render(request, 'input_form.html', {'form': form})

