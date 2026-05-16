import time
import random
import pandas as pd
from datetime import datetime

# รายชื่อสินค้าจำลอง
PRODUCTS = ['iPhone 15', 'MacBook Pro', 'AirPods 3', 'iPad Air', 'Apple Watch']
ACTIONS = ['view_product', 'add_to_cart', 'purchase']

def generate_live_click():
    """ฟังก์ชันสุ่มพฤติกรรมลูกค้าบนหน้าเว็บแบบ Real-time"""
    return {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'user_id': f"USER_{random.randint(1000, 9999)}",
        'product_name': random.choice(PRODUCTS),
        'action': random.choice(ACTIONS),
        'price': random.randint(1500, 45000)
    }

if __name__ == "__main__":
    print("🚀 เริ่มต้นระบบเว็บจำลอง: ข้อมูลกำลังสตรีมมิ่งเข้ามาแล้ว...")
    try:
        while True:
            # สุ่มสร้างข้อมูลคลิกของลูกค้า 1 รายการ
            live_data = generate_live_click()
            print(f"⚡ [Clickstream Stream] {live_data['timestamp']} | {live_data['user_id']} ทำการ {live_data['action']} สินค้า {live_data['product_name']}")
            
            # ⏳ หน่วงเวลาไว้ 1.5 วินาที เพื่อจำลองว่ามีคนกดเรื่อย ๆ
            time.sleep(1.5)
            
    except KeyboardInterrupt:
        print("\n🛑 หยุดระบบสตรีมข้อมูลชั่วคราว")