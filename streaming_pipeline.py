import time
import pandas as pd
from sqlalchemy import create_engine
from generator import generate_live_click # ดึงตัวปั๊มข้อมูลเข้ามาใช้งาน

# จำลองระบบ Cloud Storage / Cloud Data Warehouse ด้วยระบบหน่วยความจำความเร็วสูง (In-Memory Database)
# หน้างานจริงตรงนี้เราจะเปลี่ยนคำสั่งเชื่อมต่อ (Connection String) ไปหาคลังข้อมูล Google BigQuery บน Cloud ครับ
engine = create_engine('sqlite:///cloud_data_warehouse.db')

def start_realtime_pipeline(duration_seconds=30):
    """
    ฟังก์ชันดักรับข้อมูลเรียลไทม์ คลีนข้อมูล และโยนเข้าฐานข้อมูลจำลองบน Cloud
    โดยจะปล่อยให้ระบบทำงานสตรีมมิ่งเป็นเวลา 30 วินาที
    """
    print("📡 ระบบ Streaming Pipeline เปิดใช้งาน... กำลังรอรับข้อมูลแบบวินาทีต่อวินาที")
    print("----------------------------------------------------------------------")
    
    start_time = time.time()
    records_processed = 0
    
    while (time.time() - start_time) < duration_seconds:
        # 1. EXTRACT: ดักรับข้อมูลที่วิ่งมาจากหน้าเว็บเรียลไทม์
        raw_event = generate_live_click()
        
        # 2. TRANSFORM: แปลงก้อนข้อมูลให้กลายเป็นตาราง DataFrame ทันทีเพื่อประมวลผล
        df_event = pd.DataFrame([raw_event])
        
        # คลีนข้อมูลและย่อยข้อมูลแบบ Real-time (เช่น เติมชื่อสกุลเงินต่อท้ายประเภทสินค้า)
        df_event['cloud_ingested_at'] = pd.Timestamp.now() # บันทึกเวลาที่ข้อมูลวิ่งเข้าสู่ระบบ Cloud
        df_event['price_usd'] = (df_event['price'] / 35).round(2) # แปลงเงินบาทเป็นดอลลาร์สหรัฐแบบสด ๆ
        
        # 3. LOAD: ยิงข้อมูลเข้าสู่ Cloud Data Warehouse ตารางเรียลไทม์
        # 'append' หมายถึงข้อมูลใหม่โผล่มาเมื่อไหร่ ให้เอาไปต่อท้ายตารางเก่าทันทีโดยไม่ลบทิ้ง
        df_event.to_sql('realtime_clickstream', con=engine, if_exists='append', index=False)
        
        records_processed += 1
        print(f"📥 Cloud Ingestion [สำเร็จ]: ยิงข้อมูลลำดับที่ {records_processed} เข้าสู่ Cloud Database แล้ว!")
        
        # หน่วงเวลารอรับสตรีมถัดไป
        time.sleep(1)

    print("\n🏁 สรุปผล: ระบบทำการปิดรอบการสตรีมมิ่งประจำชั่วโมงเรียบร้อย")
    print(f"📊 รวมจำนวนข้อมูลที่ประมวลผลสดบน Cloud ทั้งสิ้น: {records_processed} รายการ")

if __name__ == "__main__":
    start_realtime_pipeline()