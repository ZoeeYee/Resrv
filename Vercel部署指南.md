# 🚀 Vercel 部署指南

本指南將協助您將前端和後端都部署到 Vercel。

---

## 📋 部署前準備

### 1. 確認 GitHub 倉庫已上傳
- ✅ 倉庫網址：`https://github.com/ZoeeYee/Resrv`
- ✅ 所有程式碼已 commit 並 push

### 2. 準備環境變數

#### 前端環境變數（從 `frontend/.env` 複製）：
```
VITE_FIREBASE_API_KEY=AIzaSyB1bVYNNCGBdSM_PYiPW0jbqjPAburu1-o
VITE_FIREBASE_AUTH_DOMAIN=resrvtest.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=resrvtest
VITE_FIREBASE_STORAGE_BUCKET=resrvtest.firebasestorage.app
VITE_FIREBASE_MESSAGING_SENDER_ID=89742588696
VITE_FIREBASE_APP_ID=1:89742588696:web:6ec43cd6216ce735d73c6d
VITE_API_BASE=https://你的後端網址.vercel.app
```

#### 後端環境變數（從 `backend/.env` 複製）：
```
FIREBASE_CREDENTIALS_PATH=./firebase-service-account.json
DATABASE_URL=sqlite:///./resrv.db
SECRET_KEY=你的密鑰（建議使用隨機字串）
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

> ⚠️ **重要**：Firebase 服務帳號 JSON 需要轉換為環境變數格式（見下方說明）

---

## 🎯 步驟 1：部署後端 API

### 1.1 訪問 Vercel
1. 前往 [Vercel](https://vercel.com/)
2. 使用 GitHub 帳號登入

### 1.2 創建新專案（後端）
1. 點擊 **"Add New..."** → **"Project"**
2. 選擇 `ZoeeYee/Resrv` 倉庫
3. 點擊 **"Import"**

### 1.3 配置後端專案
在專案設定頁面：

#### **Project Settings（專案設定）**
- **Project Name**: `resrv-backend`（或你喜歡的名稱）
- **Root Directory**: 選擇 `backend` 資料夾
  - 點擊 **"Edit"** → 輸入 `backend` → 點擊 **"Continue"**

#### **Framework Preset**
- 選擇 **"Other"** 或 **"Python"**

#### **Build and Output Settings**
- **Build Command**: 留空（Vercel 會自動處理）
- **Output Directory**: 留空
- **Install Command**: `pip install -r requirements.txt`

### 1.4 設定環境變數（後端）

點擊 **"Environment Variables"**，添加以下變數：

#### Firebase 服務帳號（重要！）
由於 Vercel 無法直接上傳檔案，需要將 `firebase-service-account.json` 的內容轉換為環境變數：

1. **方法一：使用環境變數（推薦）**
   - 變數名稱：`FIREBASE_CREDENTIALS`（或 `GOOGLE_APPLICATION_CREDENTIALS`）
   - 變數值：將整個 JSON 內容貼上（作為單行字串）
   - 然後在 `backend/auth.py` 中修改初始化程式碼（見下方）

2. **方法二：使用 Vercel 的環境變數**
   - 在 Vercel 專案設定中，添加以下環境變數：
     ```
     FIREBASE_PROJECT_ID=resrvtest
     FIREBASE_PRIVATE_KEY=你的私鑰
     FIREBASE_CLIENT_EMAIL=你的客戶端郵件
     ```

#### 其他環境變數：
```
DATABASE_URL=sqlite:///./resrv.db
SECRET_KEY=你的隨機密鑰（至少32字元）
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

> 💡 **提示**：`SECRET_KEY` 可以使用以下命令生成：
> ```bash
> python -c "import secrets; print(secrets.token_urlsafe(32))"
> ```

### 1.5 部署後端
1. 點擊 **"Deploy"**
2. 等待部署完成（約 1-2 分鐘）
3. 記下部署網址（例如：`https://resrv-backend.vercel.app`）

---

## 🎨 步驟 2：部署前端

### 2.1 創建新專案（前端）
1. 在 Vercel 儀表板，點擊 **"Add New..."** → **"Project"**
2. 再次選擇 `ZoeeYee/Resrv` 倉庫
3. 點擊 **"Import"**

### 2.2 配置前端專案
在專案設定頁面：

#### **Project Settings（專案設定）**
- **Project Name**: `resrv-frontend`（或你喜歡的名稱）
- **Root Directory**: 選擇 `frontend` 資料夾
  - 點擊 **"Edit"** → 輸入 `frontend` → 點擊 **"Continue"**

#### **Framework Preset**
- 選擇 **"Vite"**（Vercel 會自動偵測）

#### **Build and Output Settings**
- **Build Command**: `npm run build`（自動偵測）
- **Output Directory**: `dist`（自動偵測）
- **Install Command**: `npm install`（自動偵測）

### 2.3 設定環境變數（前端）

點擊 **"Environment Variables"**，添加以下變數：

```
VITE_FIREBASE_API_KEY=AIzaSyB1bVYNNCGBdSM_PYiPW0jbqjPAburu1-o
VITE_FIREBASE_AUTH_DOMAIN=resrvtest.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=resrvtest
VITE_FIREBASE_STORAGE_BUCKET=resrvtest.firebasestorage.app
VITE_FIREBASE_MESSAGING_SENDER_ID=89742588696
VITE_FIREBASE_APP_ID=1:89742588696:web:6ec43cd6216ce735d73c6d
VITE_API_BASE=https://你的後端網址.vercel.app
```

> ⚠️ **重要**：`VITE_API_BASE` 必須填入步驟 1.5 中獲得的後端網址！

### 2.4 部署前端
1. 點擊 **"Deploy"**
2. 等待部署完成（約 1-2 分鐘）
3. 記下部署網址（例如：`https://resrv-frontend.vercel.app`）

---

## 🔧 步驟 3：更新後端 CORS 設定

部署前端後，需要更新後端的 CORS 設定以允許前端網址：

### 3.1 更新 `backend/main.py`

將前端網址添加到 `ALLOWED_ORIGINS`：

```python
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://resrv-frontend.vercel.app",  # 你的前端網址
    "https://*.vercel.app",  # 支援所有 Vercel 子網域
]
```

### 3.2 重新部署後端
1. 在 GitHub 上 commit 並 push 更改
2. Vercel 會自動重新部署（或手動觸發）

---

## 🔥 步驟 4：處理 Firebase 服務帳號（重要）

由於 Vercel 無法直接上傳檔案，需要修改後端程式碼以從環境變數讀取 Firebase 憑證。

### 4.1 修改 `backend/auth.py`

找到 Firebase 初始化部分，修改為：

```python
# 初始化 Firebase Admin SDK
try:
    firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS")
    if firebase_cred_json:
        # 從環境變數讀取 JSON 字串
        import json
        cred_dict = json.loads(firebase_cred_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        print("✅ Firebase Admin SDK 已初始化（使用環境變數）")
    else:
        # 嘗試從檔案讀取（本地開發）
        firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
        if firebase_cred_path and os.path.exists(firebase_cred_path):
            cred = credentials.Certificate(firebase_cred_path)
            firebase_admin.initialize_app(cred)
            print("✅ Firebase Admin SDK 已初始化（使用服務帳號檔案）")
        else:
            # 使用預設應用（適用於某些部署環境）
            try:
                firebase_admin.initialize_app()
                print("✅ Firebase Admin SDK 已初始化（使用預設憑證）")
            except ValueError:
                print("⚠️  Firebase Admin SDK 可能已初始化或缺少憑證")
except Exception as e:
    print(f"⚠️  Firebase Admin SDK 初始化失敗: {e}")
    print("   將使用傳統 JWT 驗證作為後備")
```

### 4.2 在 Vercel 設定環境變數

1. 打開 `firebase-service-account.json` 檔案
2. 複製整個 JSON 內容
3. 在 Vercel 後端專案的環境變數中：
   - 變數名稱：`FIREBASE_CREDENTIALS`
   - 變數值：貼上 JSON 內容（作為單行字串，不需要格式化）

---

## ✅ 部署完成檢查清單

- [ ] 後端已部署並獲得網址
- [ ] 前端已部署並獲得網址
- [ ] 前端環境變數 `VITE_API_BASE` 已設定為後端網址
- [ ] 後端 CORS 設定已包含前端網址
- [ ] Firebase 憑證已正確設定
- [ ] 測試前端是否可以連接到後端 API
- [ ] 測試登入/註冊功能是否正常

---

## 🧪 測試部署

### 測試後端 API
1. 訪問 `https://你的後端網址.vercel.app/`
   - 應該看到：`{"msg": "Backend running successfully!"}`
2. 訪問 `https://你的後端網址.vercel.app/docs`
   - 應該看到 Swagger UI API 文件

### 測試前端
1. 訪問 `https://你的前端網址.vercel.app`
2. 嘗試註冊新帳號
3. 嘗試登入
4. 檢查瀏覽器開發者工具（F12）的 Console 和 Network 標籤

---

## 🔄 自動部署

Vercel 會自動監聽 GitHub 倉庫的變更：
- 當你 push 新的 commit 到 `main` 分支時
- Vercel 會自動重新部署前端和後端

---

## 📝 作業提交資訊（部署後）

部署完成後，你的作業提交資訊應該是：

```
前端網頁網址: https://你的前端網址.vercel.app
API伺服器網址: https://你的後端網址.vercel.app
前端網頁程式Github: https://github.com/ZoeeYee/Resrv (frontend/ 目錄)
API伺服器程式Github: https://github.com/ZoeeYee/Resrv (backend/ 目錄)
```

---

## 🆘 常見問題

### Q: 後端部署失敗？
- 檢查 `requirements.txt` 是否包含所有依賴
- 確認 Root Directory 設定為 `backend`
- 檢查環境變數是否正確設定

### Q: 前端無法連接後端？
- 確認 `VITE_API_BASE` 環境變數已設定為後端網址
- 確認後端 CORS 設定包含前端網址
- 檢查瀏覽器 Console 是否有 CORS 錯誤

### Q: Firebase 認證失敗？
- 確認 Firebase 環境變數已正確設定
- 確認 `FIREBASE_CREDENTIALS` 環境變數包含完整的 JSON
- 檢查後端日誌（Vercel 的 Functions 標籤）

### Q: 如何查看部署日誌？
1. 在 Vercel 專案頁面
2. 點擊 **"Deployments"** 標籤
3. 選擇最新的部署
4. 點擊 **"Functions"** 或 **"Build Logs"** 查看詳細資訊

---

## 📞 需要幫助？

如果遇到問題，可以：
1. 查看 Vercel 的 [官方文件](https://vercel.com/docs)
2. 檢查部署日誌找出錯誤原因
3. 確認所有環境變數都已正確設定

