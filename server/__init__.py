import http.server
import socketserver
import subprocess
import os
from urllib.parse import urlparse, parse_qs

PORT = 8010
TARGET_FOLDER = "..\excDocument"  # 的目标文件夹路径

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # 解析 URL 查询参数
            query_components = parse_qs(urlparse(self.path).query)
            file_name = query_components.get("file", [None])[0]

            if file_name:
                # 构建文件路径
                file_path = os.path.join(TARGET_FOLDER, file_name)
                # 检查路径是否是文件以及是否在目标文件夹下
                if os.path.isfile(file_path) and file_path.startswith(TARGET_FOLDER):
                    # 执行 Python 文件
                    subprocess.run(["python", file_path], check=True)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"File executed successfully")
                    return
            # 如果文件名为空或者文件不存在，返回 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found or access denied")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

def run_server():
    # 设置服务器参数
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("Server started at port", PORT)
        # 保持服务器运行
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()