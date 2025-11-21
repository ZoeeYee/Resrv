# 📤 上傳專案到 GitHub 指南

## 🎯 目標
將專案上傳到：https://github.com/ZoeeYee/Resrv

---

## 📋 步驟說明

### 步驟 1：解決 Git 所有權問題（如果需要）

如果遇到 "dubious ownership" 錯誤，執行以下命令：

```powershell
git config --global --add safe.directory F:/InteractiveHW/Resrv/Resrv
```

---

### 步驟 2：初始化 Git 倉庫（如果還沒初始化）

```powershell
# 確保在專案根目錄
cd F:\InteractiveHW\Resrv\Resrv

# 初始化 Git（如果還沒初始化）
git init
```

---

### 步驟 3：添加所有檔案

```powershell
git add .
```

**注意：** 以下檔案會被自動忽略（在 `.gitignore` 中）：
- `.env` 檔案（包含敏感資訊）
- `firebase-service-account.json`（Firebase 金鑰）
- `node_modules/`（前端依賴）
- `__pycache__/`（Python 快取）
- `*.db`（資料庫檔案）

---

### 步驟 4：建立初始提交

```powershell
git commit -m "初始提交：整合 Firebase Auth 和 Secured API"
```

---

### 步驟 5：設定分支名稱

```powershell
git branch -M main
```

---

### 步驟 6：連接 GitHub 遠端倉庫

```powershell
git remote add origin https://github.com/ZoeeYee/Resrv.git
```

如果已經有遠端倉庫，先移除再添加：
```powershell
git remote remove origin
git remote add origin https://github.com/ZoeeYee/Resrv.git
```

---

### 步驟 7：推送到 GitHub

```powershell
git push -u origin main
```

**注意：** 第一次推送時，GitHub 可能會要求你：
- 輸入 GitHub 使用者名稱
- 輸入 Personal Access Token（不是密碼）

如果沒有 Personal Access Token，需要：
1. 前往 GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 點擊 "Generate new token"
3. 選擇權限：至少需要 `repo` 權限
4. 複製 token 並在推送時使用

---

## 🔐 重要安全提醒

### ⚠️ 確保以下檔案不會被上傳：

以下檔案已經在 `.gitignore` 中，**不會**被上傳：
- ✅ `frontend/.env` - Firebase 配置（包含 API Key）
- ✅ `backend/.env` - 後端配置
- ✅ `backend/firebase-service-account.json` - Firebase 服務帳號金鑰
- ✅ `backend/resrv.db` - 資料庫檔案
- ✅ `node_modules/` - 依賴套件

### ✅ 會上傳的檔案：

- ✅ 所有程式碼檔案（`.py`, `.jsx`, `.js` 等）
- ✅ 配置檔案（`package.json`, `requirements.txt` 等）
- ✅ 文件檔案（`.md` 檔案）
- ✅ `.env.example` 範本檔案

---

## 🚀 快速上傳命令（完整流程）

如果 Git 已經可以正常使用，執行以下命令：

```powershell
# 1. 確保在專案根目錄
cd F:\InteractiveHW\Resrv\Resrv

# 2. 初始化 Git（如果還沒初始化）
git init

# 3. 添加所有檔案
git add .

# 4. 建立提交
git commit -m "初始提交：整合 Firebase Auth 和 Secured API"

# 5. 設定分支名稱
git branch -M main

# 6. 連接遠端倉庫
git remote add origin https://github.com/ZoeeYee/Resrv.git

# 7. 推送到 GitHub
git push -u origin main
```

---

## 🔍 檢查上傳狀態

### 查看哪些檔案會被提交：

```powershell
git status
```

### 查看遠端倉庫設定：

```powershell
git remote -v
```

應該看到：
```
origin  https://github.com/ZoeeYee/Resrv.git (fetch)
origin  https://github.com/ZoeeYee/Resrv.git (push)
```

---

## ❓ 常見問題

### Q: 推送時要求輸入密碼？
**A:** GitHub 不再支援密碼驗證，需要使用 Personal Access Token：
1. 前往 GitHub Settings → Developer settings → Personal access tokens
2. 建立新的 token（選擇 `repo` 權限）
3. 使用 token 作為密碼

### Q: 如何更新已上傳的檔案？
**A:** 修改檔案後：
```powershell
git add .
git commit -m "更新說明"
git push
```

### Q: 如何確認檔案已上傳？
**A:** 訪問 https://github.com/ZoeeYee/Resrv 查看倉庫內容

---

## ✅ 完成後檢查

上傳完成後，訪問 https://github.com/ZoeeYee/Resrv 應該看到：
- ✅ 所有程式碼檔案
- ✅ README.md
- ✅ 配置檔案
- ✅ 文件檔案

**不應該看到：**
- ❌ `.env` 檔案
- ❌ `firebase-service-account.json`
- ❌ `node_modules/` 目錄
- ❌ `resrv.db` 資料庫檔案

---

## 🎉 完成！

上傳完成後，你的專案就安全地儲存在 GitHub 上了！

