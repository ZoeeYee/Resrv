# 📝 Git 使用說明

## ⚠️ Commit 訊息亂碼問題

如果你在 PowerShell 中看到 commit 訊息顯示為亂碼（如：`?漱嚗?Firebase Auth ??Secured API`），這是 **PowerShell 編碼問題**，**不影響實際功能**。

### 為什麼會這樣？

- PowerShell 預設編碼可能不是 UTF-8
- Git 內部儲存是正確的（UTF-8）
- **GitHub 網頁上會正常顯示**

### 解決方法

#### 方法 1：在 GitHub 上查看（推薦）
直接訪問 https://github.com/ZoeeYee/Resrv，commit 訊息會正常顯示。

#### 方法 2：使用英文 commit 訊息
避免編碼問題，使用英文：

```powershell
git commit -m "Initial commit: Integrate Firebase Auth and Secured API"
```

#### 方法 3：設定 PowerShell UTF-8 編碼
在 PowerShell 中執行：

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001
```

---

## 📤 更新專案到 GitHub

### 基本流程

```powershell
# 1. 查看變更
git status

# 2. 添加變更的檔案
git add .

# 3. 建立提交（使用英文避免編碼問題）
git commit -m "Update: 描述你的變更"

# 4. 推送到 GitHub
git push
```

### 提交訊息範例（英文）

```powershell
git commit -m "Add Firebase authentication"
git commit -m "Update user interface"
git commit -m "Fix login bug"
git commit -m "Update documentation"
```

---

## 🔍 查看提交歷史

### 在本地查看
```powershell
git log --oneline
```

### 在 GitHub 查看（推薦）
訪問：https://github.com/ZoeeYee/Resrv/commits/main

---

## ✅ 重要提醒

1. **GitHub 上顯示正常**：雖然 PowerShell 顯示亂碼，但 GitHub 網頁上會正常顯示
2. **不影響功能**：這只是顯示問題，不影響 Git 功能
3. **建議使用英文**：如果不想看到亂碼，commit 訊息使用英文

---

## 🎯 快速指令參考

```powershell
# 查看狀態
git status

# 查看提交歷史
git log --oneline

# 添加所有變更
git add .

# 提交變更
git commit -m "你的訊息"

# 推送到 GitHub
git push

# 從 GitHub 拉取最新變更
git pull
```

