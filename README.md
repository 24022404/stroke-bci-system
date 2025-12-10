Đây là mini project sô 1  
Deadline: 16/12/2025 - Nộp báo cáo  
          06/01/2025 - Thuyết trình

# Hệ thống BCI dựa trên Motor Imagery kết hợp Feedback Thị giác cho Phục hồi Vận động Chi trên ở Bệnh nhân Đột quỵ

## Thông tin nhóm

**Tên môn học:** [Tên môn học - ví dụ: Giao diện Não-Máy tính / Brain-Computer Interface]

**Nhóm thực hiện:**

| STT | Họ và tên | Mã sinh viên | Email | Nhiệm vụ |
|-----|-----------|--------------|-------|----------|
| 1   | [Tên SV 1] | [MSSV 1] | [email@example.com] | Nghiên cứu lý thuyết, LaTeX report |
| 2   | [Tên SV 2] | [MSSV 2] | | Code demo, visualization |
| 3   | [Tên SV 3] | [MSSV 3] | | Tổng quan nghiên cứu, PowerPoint |
| 4   | [Tên SV 4] | [MSSV 4] | | Thiết kế thí nghiệm, tài liệu tham khảo |

**Thời gian thực hiện:** [Tháng năm] - [Tháng năm]

---

## 🎯 Tổng quan đề tài

### Đề bài
**Thiết kế kiến trúc hệ BCI cho đánh vần hoặc phục hồi chức năng của bệnh nhân đột quỵ**

### Chủ đề đã chọn
**Hệ thống BCI dựa trên Motor Imagery kết hợp feedback thị giác cho phục hồi vận động chi trên ở bệnh nhân đột quỵ**

### Lý do chọn chủ đề
1. **Tính cấp thiết y học:** Đột quỵ ảnh hưởng ~15 triệu người/năm, 80% bị suy giảm vận động
2. **Hiệu quả khoa học:** Motor Imagery kích hoạt neuroplasticity, hỗ trợ tái tổ chức não
3. **Tính khả thi:** Công nghệ EEG và ML hiện đại cho phép triển khai ứng dụng thực tế

---

## Cấu trúc dự án

```
stroke-bci-system/
├── README.md                          # File này
├── Report.tex                         # Báo cáo LaTeX
├── Report.pdf                         # Báo cáo đã compile (nếu có)
├── BCI_Motor_Imagery_Demo.ipynb      # Code demo Jupyter Notebook
├── Presentation.pptx                  # Slide thuyết trình (nếu có)
├── Reference/                         # Tài liệu tham khảo
│   ├── papers/                       # Papers nghiên cứu
│   └── datasets/                     # Thông tin về datasets
└── figures/                          # Hình ảnh minh họa
```

---

## 📖 Nội dung chính

### 1. Thách thức cần giải quyết

#### Thách thức về tín hiệu
- Tỷ lệ tín hiệu/nhiễu thấp (10-100 µV)
- Biến đổi không gian giữa các cá nhân
- Hiệu ứng tổn thương não ở bệnh nhân đột quỵ

#### Thách thức về phân loại
- Độ chính xác hạn chế (60-80%)
- Yêu cầu xử lý real-time (<500ms)

#### Thách thức về người dùng
- 15-30% "BCI illiterate"
- Cần duy trì động lực trong quá trình phục hồi dài hạn

### 2. Tổng quan nghiên cứu hiện tại

| Phương pháp | Ưu điểm | Nhược điểm | Accuracy |
|-------------|---------|------------|----------|
| **BCI + FES** | Cải thiện vận động tốt | Phức tạp, đắt tiền | 75-80% |
| **BCI + Robot** | Hỗ trợ vật lý trực tiếp | Rất đắt, không phù hợp tại nhà | 75-80% |
| **BCI + Visual Feedback** | Rẻ, dễ triển khai | Accuracy thấp hơn | 70-85% |

### 3. Đề xuất của nhóm

#### Phương pháp
**Common Spatial Pattern (CSP) + Linear Discriminant Analysis (LDA)**

#### Đóng góp chính
1. **Regularized CSP:** Áp dụng regularization để giảm overfitting, tăng 5-10% accuracy
2. **Adaptive Feedback System:** Feedback đa cấp độ (màu + chuyển động + âm thanh)
3. **Personalized Training Protocol:** Điều chỉnh độ khó theo từng bệnh nhân

#### Lý do chọn CSP + LDA
- **CSP:** Tối ưu hóa spatial patterns, hiệu quả với mu/beta rhythm
- **LDA:** Phân loại nhanh (<100ms), ổn định, ít overfitting
- **Kết hợp:** Cân bằng giữa accuracy và tốc độ cho real-time BCI

### 4. Thiết kế thí nghiệm

#### Dataset
- **BCI Competition IV - Dataset 2a** hoặc **PhysioNet Motor Imagery**
- 2 class: Left hand vs Right hand
- 288-360 trials/subject

#### Experiments
1. **Experiment 1:** Đánh giá CSP+LDA vs baseline methods
2. **Experiment 2:** Tối ưu regularization parameter (λ)
3. **Experiment 3:** Simulation real-time với latency <500ms

#### Kết quả kỳ vọng
- Accuracy: **80-90%** (cao hơn 5-10% so với baseline)
- Latency: **<300ms**
- BCI illiteracy: giảm xuống **10-15%**

---

## Code Demo

### Yêu cầu hệ thống
```bash
Python >= 3.7
numpy
matplotlib
seaborn
scipy
scikit-learn
```

### Cài đặt
```bash
# Clone repository
git clone [repository-url]
cd stroke-bci-system

# Cài đặt dependencies
pip install numpy matplotlib seaborn scipy scikit-learn jupyter
```

### Chạy demo
```bash
# Mở Jupyter Notebook
jupyter notebook BCI_Motor_Imagery_Demo.ipynb

# Hoặc chạy trực tiếp
jupyter nbconvert --to notebook --execute BCI_Motor_Imagery_Demo.ipynb
```

### Nội dung demo
1. Load và visualize EEG data (synthetic)
2. Bandpass filtering (8-30 Hz)
3. CSP implementation với regularization
4. LDA classification
5. Plots: Confusion matrix, accuracy, CSP patterns, feature space

**Lưu ý:** Code demo sử dụng **dữ liệu giả lập** (synthetic data) để minh họa concept. Trong thực tế, có thể load dataset công khai từ BCI Competition hoặc PhysioNet.

---

## 📊 Kết quả chính

### Từ báo cáo LaTeX

- **Chủ đề cụ thể:** Motor Imagery BCI với visual feedback
- **Literature review:** So sánh 3 phương pháp chính
- **Phương pháp đề xuất:** CSP + LDA với regularization
- **Đóng góp:** 3 cải tiến (Regularized CSP, Adaptive Feedback, Personalized Protocol)
- **Thiết kế thí nghiệm:** 3 experiments với metrics rõ ràng

### Từ code demo

- **CSP filters:** Học được spatial patterns phân biệt 2 class
- **Accuracy:** Đạt 75-90% trên synthetic data
- **Visualization:** Confusion matrix, CSP patterns, feature space
- **Regularization:** Cải thiện generalization

---

## Tài liệu tham khảo

Xem chi tiết trong file `Report.tex` phần References:

1. Ramos-Murguialday, A., et al. (2013). Brain-machine interface in chronic stroke rehabilitation
2. Ang, K. K., et al. (2014). EEG-based motor imagery BCI robotic rehabilitation
3. Lotte, F., et al. (2018). Classification algorithms for EEG-based BCIs: 10 year update
4. Pfurtscheller, G., & Neuper, C. (2006). ERD/ERS in BCI developments
5. Blankertz, B., et al. (2008). Optimizing spatial filters for robust EEG analysis

---

## 🎓 Phạm vi dự án

### ✅ Đã hoàn thành

- [x] Chọn chủ đề cụ thể
- [x] Phân tích lý do và thách thức
- [x] Tổng quan nghiên cứu hiện tại
- [x] Đề xuất phương pháp và đóng góp
- [x] Trình bày chi tiết phương pháp (CSP, LDA, ERD)
- [x] Thiết kế thí nghiệm
- [x] Báo cáo LaTeX hoàn chỉnh (8 trang)
- [x] Code demo minh họa concept
- [x] Visualization (plots, confusion matrix)

### ⚠️ Lưu ý quan trọng

**Đây là dự án ở mức LÝ THUYẾT:**

- ❌ **KHÔNG** thực hiện thí nghiệm thực tế
- ❌ **KHÔNG** thu thập dữ liệu EEG từ bệnh nhân
- ❌ **KHÔNG** triển khai hệ thống hoàn chỉnh
- ✅ **CHỈ** thiết kế kiến trúc và phương pháp
- ✅ **CHỈ** code demo để minh họa "concept works"

### 🔄 Có thể bổ sung (optional)

- [ ] PowerPoint presentation
- [ ] Thử nghiệm trên dataset thực (BCI Competition)
- [ ] Deep learning comparison (CNN, EEGNet)
- [ ] Interactive feedback visualization (Unity/Pygame)

---

## 📝 Cách sử dụng repository

### Đọc báo cáo
```bash
# Compile LaTeX (nếu cần)
pdflatex Report.tex
bibtex Report
pdflatex Report.tex
pdflatex Report.tex

# Hoặc đọc file PDF có sẵn
```

### Chạy code demo
```bash
jupyter notebook BCI_Motor_Imagery_Demo.ipynb
# Chạy từng cell theo thứ tự
```

### Chuẩn bị presentation
```bash
# Sử dụng nội dung từ Report.tex
# Tóm tắt các phần chính:
# 1. Giới thiệu và động lực
# 2. Thách thức
# 3. Phương pháp đề xuất
# 4. Kết quả mô phỏng
# 5. Kết luận và hướng phát triển
```

---
## License

Dự án này được thực hiện cho mục đích học tập và nghiên cứu.

---

**© 2025 - Nhóm [Tên nhóm] - [Tên trường/khoa]**
