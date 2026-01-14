import os
import webbrowser
from playwright.sync_api import sync_playwright

class BrowserHelper:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def open_in_browser(self, url):
        """直接在用户默认浏览器打开网页"""
        try:
            webbrowser.open(url)
            return f"Successfully opened {url} in your default browser."
        except Exception as e:
            return f"Failed to open browser: {str(e)}"

    def capture_screenshot(self, url, filename="screenshot.png"):
        """后台打开网页并截图"""
        output_path = os.path.join(self.root_dir, filename)
        try:
            with sync_playwright() as p:
                # 启动无头浏览器
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                # 设置视图大小（模拟标准桌面）
                page.set_viewport_size({"width": 1280, "height": 720})
                
                print(f"Navigating to {url}...")
                page.goto(url, wait_until="networkidle")
                
                # 截图并保存
                page.screenshot(path=output_path, full_page=True)
                browser.close()
                
            return f"Screenshot saved to {filename}. You can now add this file to chat to let AI 'see' it."
        except Exception as e:
            return f"Error capturing screenshot: {str(e)}"