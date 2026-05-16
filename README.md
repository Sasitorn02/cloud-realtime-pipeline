# Real-time E-commerce Clickstream Pipeline on Cloud

โปรเจคจำลองระบบการดักรับและประมวลข้อมูลพฤติกรรมการใช้งานหน้าเว็บของลูกค้า (Clickstream Data) แบบวินาทีต่อวินาที (Real-time Streaming) และทำการจัดส่งข้อมูลเข้าสู่คลังข้อมูลจำลองบนระบบ Cloud (Cloud Data Warehouse) เพื่อนำไปวิเคราะห์พฤติกรรมผู้บริโภคทันที

## 🛠️ Tech Stack ที่ใช้
- **Language:** Python 3.11
- **Libraries:** Pandas, SQLAlchemy, Time
- **Database:** Cloud Storage / Data Warehouse Mockup (SQLite Memory Engine)

## 🔄 กระบวนการ Real-time Streaming
1. **Data Generation:** จำลองพฤติกรรมลูกค้า (การดูสินค้า, การกดใส่ตะกร้า, การสั่งซื้อ) สตรีมเข้ามาในระบบทุก ๆ 1-1.5 วินาทีแบบต่อเนื่อง
2. **Real-time Transform:** ดักรับข้อมูลก้อนสด นำมาแปลงเป็นตารางด้วย Pandas คลีนข้อมูล และคำนวณแปลงค่าเงินบาทเป็น USD หน้างานทันที พร้อมประทับตราเวลาที่ข้อมูลเข้าสู่ระบบ Cloud (`cloud_ingested_at`)
3. **Continuous Load:** ใช้โหมด `append` ยิงข้อมูลใหม่เข้าไปต่อท้ายฐานข้อมูลปลายทางทันทีโดยไม่มีการบล็อกระบบ เพื่อรองรับข้อมูลที่ไหลมาไม่หยุด