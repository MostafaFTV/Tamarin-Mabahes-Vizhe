import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# فرض می‌کنیم مدل آموزش دیده شده قبلاً ذخیره شده است
model = load_model('path_to_your_saved_model.h5')

def test_images(model, test_images_dir):
    correct_predictions = 0
    total_predictions = 0

    # لیستی از مسیرهای تصاویر آزمایشی
    test_images_paths = [test_images_dir + f'/image_{i}.jpg' for i in range(1, 101)]

    for img_path in test_images_paths:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        prediction = model.predict(img_array)
        if prediction[0][0] > 0.5:
            print(f'{img_path} is a dog')
        else:
            print(f'{img_path} is a cat')

        # اینجا باید منطق تشخیص صحیح را بر اساس برچسب‌های واقعی اضافه کنید
        # if (prediction is correct according to the true label):
        #     correct_predictions += 1
        total_predictions += 1

    accuracy = (correct_predictions / total_predictions) * 100
    print(f'Accuracy: {accuracy}%')

# مسیر پوشه حاوی تصاویر آزمایشی را اینجا قرار دهید
test_images_dir = 'path_to_your_test_images_folder'
test_images(model, test_images_dir)
