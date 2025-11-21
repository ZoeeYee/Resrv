# 🔧 Vercel 後端錯誤排除指南

## 錯誤：500 INTERNAL_SERVER_ERROR / FUNCTION_INVOCATION_FAILED

### 步驟 1：查看錯誤日誌

1. 在 Vercel 專案頁面
2. 點擊 **"Deployments"** 標籤
3. 選擇最新的部署（失敗的那個）
4. 點擊部署項目，查看詳細資訊
5. 點擊 **"Functions"** 或 **"Runtime Logs"** 標籤
6. 查看錯誤訊息

### 步驟 2：常見問題和解決方案

#### 問題 1：Firebase 憑證格式錯誤

**錯誤訊息**：`JSONDecodeError` 或 `Invalid credentials`

**解決方法**：
1. 在 Vercel 專案設定中，找到環境變數 `FIREBASE_CREDENTIALS`
2. 確認 Value 是完整的 JSON 字串（單行，沒有換行）
3. 格式應該是：
   ```
   {"type":"service_account","project_id":"resrvtest",...}
   ```
4. 不要有多餘的空格或換行
5. 重新部署

#### 問題 2：缺少依賴

**錯誤訊息**：`ModuleNotFoundError` 或 `ImportError`

**解決方法**：
1. 確認 `backend/requirements.txt` 包含所有必要的套件
2. 在 Vercel 專案設定中，確認 **Install Command** 是：`pip install -r requirements.txt`

#### 問題 3：資料庫初始化錯誤

**錯誤訊息**：資料庫相關錯誤

**解決方法**：
- 在 Serverless 環境中，SQLite 可能無法正常運作
- 建議使用 PostgreSQL（如 Vercel Postgres）或暫時跳過資料庫初始化

#### 問題 4：Python 路徑問題

**錯誤訊息**：`ModuleNotFoundError` 或找不到模組

**解決方法**：
- 確認 `backend/api/index.py` 正確導入 `main.py`
- 確認 Root Directory 設定為 `backend`

### 步驟 3：檢查環境變數

確認以下環境變數都已正確設定：

- ✅ `FIREBASE_CREDENTIALS` - Firebase 服務帳號 JSON（單行字串）
- ✅ `DATABASE_URL` - 資料庫連接字串
- ✅ `SECRET_KEY` - JWT 密鑰
- ✅ `ALGORITHM` - HS256
- ✅ `ACCESS_TOKEN_EXPIRE_MINUTES` - 60

### 步驟 4：測試修正

1. 修正問題後，在 Vercel 中：
   - 點擊 **"Redeploy"** 重新部署
   - 或 push 新的 commit 到 GitHub（會自動重新部署）

2. 測試 API：
   - 訪問：`https://你的後端網址.vercel.app/`
   - 應該看到：`{"msg": "Backend running successfully!"}`

### 步驟 5：如果還是失敗

1. **查看完整錯誤日誌**：
   - 在 Vercel 的 Functions 標籤中查看詳細錯誤
   - 複製錯誤訊息

2. **簡化測試**：
   - 暫時移除 Firebase 初始化，測試基本 API 是否正常
   - 逐步添加功能，找出問題所在

3. **檢查程式碼**：
   - 確認所有 import 都正確
   - 確認沒有使用本地檔案系統的功能

## 快速檢查清單

- [ ] 環境變數都已設定
- [ ] `FIREBASE_CREDENTIALS` 格式正確（單行 JSON）
- [ ] Root Directory 設定為 `backend`
- [ ] `requirements.txt` 包含所有依賴
- [ ] 查看錯誤日誌找出具體問題
- [ ] 測試基本 API 端點（`/`）

