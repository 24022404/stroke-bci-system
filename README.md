# BCI Motor Imagery - Stroke Rehabilitation System

Hệ thống giao diện não-máy tính phân loại tín hiệu Motor Imagery từ EEG, ứng dụng trong phục hồi chức năng vận động cho bệnh nhân đột quỵ.

---

## Dataset

BCI Competition IV Dataset 2a
- 9 subjects
- 4 classes: Left hand, Right hand, Feet, Tongue  
- 22 kênh EEG, 250 Hz

---

## Pipeline

```
Raw Data (.gdf)
    ↓
Preprocessing (Filter, CAR, AutoReject)
    ↓
Feature Extraction (CSP)
    ↓
Classification (LDA)
    ↓
Visual Feedback (Game)
```

---

## Cấu trúc thư mục

```
stroke-bci-system/
├── data/                          # Dữ liệu thô
├── processed_data/                # Dữ liệu đã xử lý
├── features_data/                 # Đặc trưng CSP
├── 01_Data_Loading_and_Exploration.ipynb
├── 02_Preprocessing.ipynb
├── 03_Feature_Extraction.ipynb
├── 04_Classification.ipynb
├── 05_Visual_Feedback.py
```

---

## Chạy dự án

**Tiền xử lý:**
```bash
jupyter notebook 02_Preprocessing.ipynb
```

**Trích xuất đặc trưng:**
```bash
jupyter notebook 03_Feature_Extraction.ipynb
```

**Phân loại:**
```bash
jupyter notebook 04_Classification.ipynb
```

**Visual Feedback**
```bash
python 05_Visual_Feedback.py
```

---

## Thành viên nhóm

1. Đồng Mạnh Hùng - 23020370
2. Phạm Anh Quân - 22022625
3. Cao Đăng Quốc Vương - 22022601
4. Nguyễn Văn Thân - 22022596
5. Nguyễn Đức Minh - 24022404
6. Nguyễn Xuân Hiệp - 22022591
7. Lương Minh Trí - 23020440

---

## Phân công công việc

Xem chi tiết phân công tại:

[Google Docs - Phân công công việc](https://docs.google.com/document/d/1eO2_duQ4NBcamuUVNSQwDjzRrpXCIayeIve0vwcr0LE/edit?hl=vi&tab=t.0)

---

## Timeline

- Nộp báo cáo: 16/12/2025
- Thuyết trình: 06/01/2025

---

## Tài liệu tham khảo

1. BCI Competition IV Dataset 2a: http://www.bbci.de/competition/iv/desc_2a.pdf
2. MNE-Python: https://mne.tools/
