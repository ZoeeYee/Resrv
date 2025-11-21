# 🔥 Firebase Auth 整合配置指南

本指南將幫助你完成 Firebase Authentication 的配置，使前端和後端能夠正常工作。

## 📋 前置要求

1. 一個 Google 帳號
2. 訪問 Firebase Console 的權限

---

## 🚀 步驟 1: 建立 Firebase 專案

1. 訪問 [Firebase Console](https://console.firebase.google.com/)
2. 點擊「新增專案」或「Create a project」
3. 輸入專案名稱（例如：`resrv-app`）
4. 按照提示完成專案建立

---

## 🔧 步驟 2: 啟用 Authentication

1. 在 Firebase Console 中，點擊左側選單的「Authentication」
2. 點擊「Get started」
3. 在「Sign-in method」標籤頁中，啟用「Email/Password」：
   - 點擊「Email/Password」
   - 啟用第一個開關（Email/Password）
   - 點擊「Save」

---

## 📱 步驟 3: 取得前端配置資訊

1. 在 Firebase Console 中，點擊左側選單的「專案設定」（齒輪圖示）
2. 向下滾動到「你的應用」部分
3. 點擊「Web」圖示（`</>`）新增 Web 應用
4. 輸入應用暱稱（例如：`Resrv Web App`）
5. 點擊「註冊應用」
6. 複製顯示的配置物件，它看起來像這樣：

```javascript
const firebaseConfig = {
  apiKey: "AIzaSy...",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef"
};
```

---

## ⚙️ 步驟 4: 設定前端環境變數

1. 在 `frontend` 目錄下建立 `.env` 檔案（如果不存在）
2. 新增以下環境變數：

```env
# Firebase 配置
VITE_FIREBASE_API_KEY=你的-api-key
VITE_FIREBASE_AUTH_DOMAIN=你的專案.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=你的專案-id
VITE_FIREBASE_STORAGE_BUCKET=你的專案.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=你的-sender-id
VITE_FIREBASE_APP_ID=你的-app-id

# 後端 API 位址
VITE_API_BASE=http://localhost:8000
```

3. 將步驟 3 中複製的配置值填入對應的環境變數

---

## 🔐 步驟 5: 設定後端 Firebase Admin SDK

後端需要 Firebase Admin SDK 來驗證 Firebase JWT token。有兩種配置方式：

### 方式 A: 使用服務帳號金鑰檔案（推薦用於本地開發）

1. 在 Firebase Console 中，點擊「專案設定」
2. 切換到「服務帳號」標籤頁
3. 點擊「產生新的私鑰」
4. 下載 JSON 檔案（例如：`firebase-service-account.json`）
5. 將檔案放在 `backend` 目錄下
6. **重要：** 將檔案新增到 `.gitignore`，不要提交到 Git！

```bash
# 在 backend/.gitignore 中新增
firebase-service-account.json
*.json
```

7. 在 `backend` 目錄建立 `.env` 檔案，新增：

```env
# Firebase Admin SDK 配置
FIREBASE_CREDENTIALS_PATH=./firebase-service-account.json

# 其他配置
DATABASE_URL=sqlite:///./resrv.db
SECRET_KEY=your-secret-key-here
```

### 方式 B: 使用環境變數（推薦用於生產環境）

在生產環境（如 Vercel、Heroku）中，可以設定環境變數而不是使用檔案。

---

## ✅ 步驟 6: 驗證配置

### 前端驗證

1. 啟動前端開發伺服器：
   ```bash
   cd frontend
   npm run dev
   ```

2. 開啟瀏覽器訪問 `http://localhost:5173`
3. 嘗試註冊一個新帳號
4. 檢查瀏覽器控制台是否有錯誤

### 後端驗證

1. 啟動後端伺服器：
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. 查看啟動日誌，應該看到：
   ```
   ✅ Firebase Admin SDK 已初始化（使用服務帳號檔案）
   ```

3. 訪問 `http://localhost:8000/docs` 查看 API 文件
4. 嘗試呼叫 `/auth/me` 端點（需要先登入取得 token）

---

## 🧪 測試流程

1. **註冊新使用者**：
   - 在前端點擊「註冊」
   - 輸入姓名、Email 和密碼
   - 點擊「註冊」
   - 應該自動登入並顯示使用者資訊

2. **登入**：
   - 如果已註冊，點擊「登入」
   - 輸入 Email 和密碼
   - 應該成功登入

3. **驗證 API**：
   - 登入後，前端會自動取得 Firebase ID Token
   - Token 會傳送到後端 `/auth/me` 端點
   - 後端會驗證 token 並回傳使用者資訊

---

## 🔍 故障排除

### 問題 1: 前端 Firebase 初始化失敗

**症狀**：瀏覽器控制台顯示 Firebase 錯誤

**解決方案**：
- 檢查 `.env` 檔案中的 Firebase 配置是否正確
- 確認所有環境變數都以 `VITE_` 開頭
- 重新啟動開發伺服器

### 問題 2: 後端 Firebase Admin SDK 初始化失敗

**症狀**：啟動時看到 `⚠️ Firebase Admin SDK 初始化失敗`

**解決方案**：
- 檢查 `FIREBASE_CREDENTIALS_PATH` 是否正確
- 確認服務帳號 JSON 檔案存在且格式正確
- 檢查檔案路徑是否為相對路徑（從 `backend` 目錄）

### 問題 3: Token 驗證失敗

**症狀**：呼叫 `/auth/me` 回傳 401 錯誤

**解決方案**：
- 確認前端正確取得並傳送了 Firebase ID Token
- 檢查後端日誌中的錯誤資訊
- 確認 Firebase Admin SDK 已正確初始化

### 問題 4: 使用者註冊後無法登入

**症狀**：註冊成功但登入失敗

**解決方案**：
- 檢查 Firebase Console 中的 Authentication 使用者列表
- 確認 Email/Password 認證已啟用
- 檢查瀏覽器控制台的錯誤資訊

---

## 📝 重要注意事項

1. **安全性**：
   - ⚠️ **永遠不要**將 Firebase 服務帳號金鑰檔案提交到 Git
   - ⚠️ **永遠不要**在前端程式碼中暴露 Firebase Admin SDK 憑證
   - ✅ 使用環境變數儲存敏感資訊

2. **資料庫遷移**：
   - 如果已有使用者資料，需要執行資料庫遷移
   - 新的 `firebase_uid` 欄位是可選的，不會影響現有使用者

3. **相容性**：
   - 系統同時支援 Firebase Auth 和傳統 JWT 認證
   - 新使用者使用 Firebase，舊使用者仍可使用傳統方式登入

---

## 🎉 完成！

配置完成後，你的應用現在使用 Firebase Authentication 進行使用者認證，後端 API 會驗證 Firebase JWT token 來保護 API 端點。

如有問題，請檢查：
- Firebase Console 中的配置
- 前端和後端的日誌輸出
- 瀏覽器開發者工具的網路請求

