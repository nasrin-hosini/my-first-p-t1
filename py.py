#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ماژول ماشین حساب ساده
این ماژول شامل توابع پایه‌ای ریاضی برای یک ماشین حساب ساده است.
نوشته شده توسط: [اسم خودت رو بنویس]
تاریخ: فوریه ۲۰۲۶
"""

class SimpleCalculator:
    """
    یک کلاس ماشین حساب ساده با قابلیت ذخیره تاریخچه عملیات
    
    Attributes:
        name (str): نام ماشین حساب
        history (list): لیست تاریخچه عملیات انجام شده
    """
    
    def __init__(self, name="MyCalculator"):
        """
        سازنده کلاس - مقداردهی اولیه ماشین حساب
        
        Args:
            name (str): نام دلخواه برای ماشین حساب (پیش‌فرض: MyCalculator)
        """
        self.name = name
        self.history = []
        print(f"✅ ماشین حساب '{self.name}' با موفقیت ایجاد شد!")
    
    def add(self, a, b):
        """
        جمع دو عدد
        
        Args:
            a (float): عدد اول
            b (float): عدد دوم
        
        Returns:
            float: حاصل جمع a و b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """
        تفریق دو عدد
        
        Args:
            a (float): عدد اول
            b (float): عدد دوم
        
        Returns:
            float: حاصل تفریق a منهای b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """
        ضرب دو عدد
        
        Args:
            a (float): عدد اول
            b (float): عدد دوم
        
        Returns:
            float: حاصل ضرب a در b
        """
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """
        تقسیم دو عدد
        
        Args:
            a (float): عدد اول (مقسوم)
            b (float): عدد دوم (مقسوم‌علیه)
        
        Returns:
            float: حاصل تقسیم a بر b
            
        Raises:
            ValueError: اگر b برابر صفر باشد
        """
        if b == 0:
            raise ValueError("❌ خطا: تقسیم بر صفر مجاز نیست!")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        """
        توان رساندن عدد a به توان b
        
        Args:
            a (float): پایه
            b (float): توان
        
        Returns:
            float: a به توان b
        """
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def show_history(self):
        """نمایش تاریخچه عملیات انجام شده"""
        if not self.history:
            print("📭 تاریخچه خالی است!")
        else:
            print(f"📋 تاریخچه عملیات '{self.name}':")
            for i, item in enumerate(self.history, 1):
                print(f"   {i}. {item}")
    
    def clear_history(self):
        """پاک کردن تاریخچه"""
        self.history.clear()
        print("🧹 تاریخچه پاک شد!")
    
    def about(self):
        """اطلاعات درباره ماشین حساب"""
        print(f"""
╔══════════════════════════════╗
║     درباره ماشین حساب        ║
╠══════════════════════════════╣
║ نام: {self.name}
║ نسخه: 1.0.0
║ عملیات: جمع، تفریق، ضرب، تقسیم، توان
║ تاریخچه: {len(self.history)} عملیات
╚══════════════════════════════╝
        """)


def main():
    """
    تابع اصلی برای اجرای برنامه
    این تابع یک نمونه از ماشین حساب می‌سازد و چند عملیات نمونه انجام می‌دهد
    """
    print("=" * 50)
    print("🚀 شروع کار با ماشین حساب ساده")
    print("=" * 50)
    
    # ساخت یک نمونه از ماشین حساب
    calc = SimpleCalculator("محاسبه‌گر من")
    
    # انجام چند عملیات نمونه
    print("\n📝 انجام عملیات نمونه:")
    
    # جمع
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")
    
    # ضرب
    result = calc.multiply(4, 3)
    print(f"4 × 3 = {result}")
    
    # تقسیم
    try:
        result = calc.divide(15, 3)
        print(f"15 ÷ 3 = {result}")
    except ValueError as e:
        print(e)
    
    # توان
    result = calc.power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    # نمایش تاریخچه
    print("\n" + "=" * 50)
    calc.show_history()
    
    # اطلاعات ماشین حساب
    print("\n" + "=" * 50)
    calc.about()
    
    print("\n✨ برنامه با موفقیت اجرا شد!")


if __name__ == "__main__":
    main()