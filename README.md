Dưới đây là phiên bản README.md chuyên nghiệp bằng tiếng Việt dành cho dự án của bạn trên GitHub:

---

# Fuutoru Docker API Ollama

Ứng dụng nhẹ được đóng gói bằng Docker, tích hợp FastAPI và Ollama để phân tích cảm xúc của văn bản liên quan đến tập đoàn "ggroup". Dự án sử dụng mô hình `llama3.2:1b` để phân loại cảm xúc thành ba nhãn: Trung lập (NEU), Tích cực (POS), và Tiêu cực (NEG).

## Cấu trúc dự án

```
fuutoru-docker-api-ollama/
├── docker-compose.yml         # Cấu hình Docker Compose
├── fastapi/                   # Thư mục dịch vụ FastAPI
│   ├── app.py                 # Ứng dụng FastAPI chính
│   ├── Dockerfile             # Dockerfile cho dịch vụ FastAPI
│   └── requirements.txt       # Các phụ thuộc Python
└── ollama/                    # Thư mục dịch vụ Ollama
    ├── Dockerfile             # Dockerfile cho dịch vụ Ollama
    └── pull-llama3.sh         # Script để tải và chạy mô hình llama3.2:1b
```

## Tính năng

- **Phân tích cảm xúc**: Phân tích văn bản đầu vào để xác định cảm xúc (NEU, POS, NEG) bằng mô hình `llama3.2:1b`.
- **Dịch vụ Docker**: Chạy FastAPI và Ollama trong các container độc lập để dễ triển khai và mở rộng.
- **Điểm cuối API**: Cung cấp điểm cuối GET đơn giản (`/ask`) để xử lý văn bản và trả về nhãn cảm xúc.

## Yêu cầu cài đặt

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Hướng dẫn cài đặt

1. **Sao chép kho lưu trữ**:
   ```bash
   git clone https://github.com/yourusername/fuutoru-docker-api-ollama.git
   cd fuutoru-docker-api-ollama
   ```

2. **Xây dựng và chạy dịch vụ**:
   ```bash
   docker-compose up --build
   ```
   Lệnh này xây dựng hình ảnh FastAPI và Ollama, sau đó khởi động các container. Dịch vụ Ollama sẽ tự động tải mô hình `llama3.2:1b` trong lần chạy đầu tiên.

3. **Kiểm tra dịch vụ**:
   - FastAPI sẽ khả dụng tại `http://localhost:8000`.
   - Ollama sẽ khả dụng tại `http://localhost:11434`.

## Cách sử dụng

### Điểm cuối API

1. **Kiểm tra trạng thái**:
   - **Điểm cuối**: `GET /`
   - **Phản hồi**: `{"status": "Ok"}`
   - **Mô tả**: Kiểm tra xem dịch vụ FastAPI có đang chạy không.

   Ví dụ:
   ```bash
   curl http://localhost:8000/
   ```

2. **Phân tích cảm xúc**:
   - **Điểm cuối**: `GET /ask?prompt=<văn-bản-của-bạn>`
   - **Phản hồi**: Một trong `NEU`, `POS`, hoặc `NEG`
   - **Mô tả**: Phân tích cảm xúc của văn bản được cung cấp liên quan đến "ggroup".

   Ví dụ:
   ```bash
   curl "http://localhost:8000/ask?prompt=Tập%20đoàn%20ggroup%20rất%20tuyệt%20vời"
   ```
   Phản hồi: `POS`

### Ví dụ minh họa

- Đầu vào: `"Tập đoàn ggroup hoạt động kém hiệu quả"`
  - Đầu ra: `NEG`
- Đầu vào: `"Tôi không có ý kiến gì về tập đoàn ggroup"`
  - Đầu ra: `NEU`
- Đầu vào: `"Tập đoàn ggroup đang phát triển mạnh mẽ"`
  - Đầu ra: `POS`

## Cấu hình

- **Cổng**:
  - FastAPI: `8000`
  - Ollama: `11434`
- **Volume**:
  - Mã nguồn FastAPI được gắn kết để hỗ trợ tải lại trực tiếp trong quá trình phát triển.
  - Ollama lưu trữ dữ liệu mô hình trong volume Docker `ollama_volume`.

## Phát triển

Để chỉnh sửa ứng dụng FastAPI:
1. Sửa đổi `fastapi/app.py`.
2. Các thay đổi sẽ được tải lại tự động nhờ cờ `--reload` trong Dockerfile của FastAPI.

Để sử dụng mô hình khác:
1. Cập nhật trường `model` trong `fastapi/app.py` (ví dụ: thay `llama3.2:1b` bằng mô hình khác).
2. Sửa đổi `ollama/pull-llama3.sh` để tải mô hình mong muốn.

## Khắc phục sự cố

- **Dịch vụ không khởi động**: Kiểm tra nhật ký Docker bằng `docker-compose logs`.
- **Mô hình không tải được**: Đảm bảo container Ollama có kết nối internet để tải mô hình `llama3.2:1b`.
- **Lỗi API**: Xác minh dịch vụ Ollama đang chạy và có thể truy cập tại `http://ollama:11434`.

## Đóng góp

Hãy thoải mái gửi vấn đề hoặc yêu cầu kéo để cải thiện dự án này. Vui lòng tuân theo quy trình làm việc tiêu chuẩn của GitHub khi đóng góp.

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT. Xem tệp [LICENSE](LICENSE) để biết chi tiết.

## Lời cảm ơn

- [FastAPI](https://fastapi.tiangolo.com/) cho framework web.
- [Ollama](https://ollama.ai/) cho việc cung cấp mô hình `llama3.2:1b` và môi trường chạy.

---

Phiên bản này được viết bằng tiếng Việt, rõ ràng và chuyên nghiệp, phù hợp để sử dụng trên GitHub. Hãy thay `yourusername` trong URL clone bằng tên người dùng GitHub thực tế của bạn. Nếu bạn muốn điều chỉnh thêm, hãy cho tôi biết!
