import random

def obscure_function():
    # توليد نصوص عشوائية تحتوي على رموز مختلفة
    part1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=15))
    part2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
    part3 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=20))
    part4 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))

    # إدراج @ و H في أماكن غير متوقعة
    encoded_message = f"{part1}H{part2}@{part3}{part4}"

    # طباعة النص المشفر
    print("النص المشفر هو:")
    print(encoded_message)

    # التحقق من النص
    def check_message(message):
        # التحقق إذا كان يحتوي على الرمزين @ و H
        if '@' in message and 'H' in message:
            return True
        return False

    if check_message(encoded_message):
        print("تهانينا! لقد وجدت الرمزين. انتقل إلى [التالي](challenge.html) لحل التحدي التالي.")
    else:
        print("النص لا يحتوي على الرمزين المطلوبين.")

# تشغيل الدالة المشفرة
obscure_function()
