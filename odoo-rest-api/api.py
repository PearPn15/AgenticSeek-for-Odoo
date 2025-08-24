import json
import requests
import sys

AUTH_URL = 'http://localhost:8069/auth/'
headers = {'Content-type': 'application/json'}

# --- 1. Xác thực ---
auth_data = {
    'params': {
         'login': 'admin',
         'password': '12345',
         'db': 'namle'
    }
}

# Gửi yêu cầu xác thực
auth_res = requests.post(
    AUTH_URL, 
    data=json.dumps(auth_data), 
    headers=headers
)

# Lưu lại cookie sau khi xác thực thành công
cookies = auth_res.cookies
print("--- Authentication Successful ---")


# # --- 2. Lấy dữ liệu Người dùng (Users) ---
# users_url = 'http://localhost:8069/api/res.users/' # ✅ Tên biến rõ ràng

# # Gửi yêu cầu lấy danh sách người dùng
# users_res = requests.get(
#     users_url, 
#     cookies=cookies
# )

# print("\n--- Users Data ---")
# print(users_res.text)


# --- 3. Lấy dữ liệu Sản phẩm (Products) ---
products_url = 'http://localhost:8069/api/project.project/' # ✅ Tên biến rõ ràng

# Chỉ định chỉ lấy trường id và name để request nhanh hơn
products_params = {'query': '{id, name}'}

# Gửi yêu cầu lấy danh sách sản phẩm
products_res = requests.get(
    products_url, 
    params=products_params,
    cookies=cookies
)

print("\n--- project Data (ID and Name only) ---")
print(products_res.text)