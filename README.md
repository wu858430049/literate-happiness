## Move Files to Parent

### Description

The `move-files-to-parent` script is designed to move all contents (files and directories) from subdirectories to their parent directory. It also removes any empty subdirectories after the contents have been moved. This script is useful for organizing files by consolidating all items from nested directories into a single parent directory.

### Features

- **Move Files**: Automatically move all files from subdirectories to the specified parent directory.
- **Move Directories**: Move entire directories from subdirectories to the parent directory if they do not already exist in the parent directory.
- **Cleanup**: Remove any empty subdirectories after moving their contents.

### Requirements

- Python 3.x
- Permissions to read/write in the source directory

### Usage

1. **Prepare the Environment**: Ensure you have Python 3 installed on your system. Install any necessary dependencies if required.

2. **Edit and Run the Script**:
    - Save the script as `move_files.py`.
    - Run the script using a Python interpreter and provide the source directory path when prompted.

3. **Command to Run the Script**:
    ```shell
    python move_files.py
    ```

4. **Input Source Directory**: When prompted, enter the full path to the directory containing subdirectories whose contents need to be moved.

### Example

```shell
Enter the source directory: /path/to/your/source/directory
Starting to process the source directory: /path/to/your/source/directory
...
文件移動完成!
```



---

## 移動文件到父目錄

### 描述

`move-files-to-parent` 腳本旨在將所有內容（文件和目錄）從子目錄移動到其父目錄。移動內容後，它還會刪除任何空的子目錄。此腳本有助於通過將嵌套目錄中的所有項目集中到一個父目錄中來組織文件。

### 功能

- **移動文件**：自動將所有文件從子目錄移動到指定的父目錄。
- **移動目錄**：將整個目錄從子目錄移動到父目錄（如果目標目錄中不存在）。
- **清理**：在移動內容後刪除任何空的子目錄。

### 要求

- Python 3.x
- 對源目錄具有讀寫權限

### 使用方法

1. **準備環境**：確保你的系統上已安裝Python 3。如有需要，安裝任何必要的依賴項。

2. **編輯並運行腳本**：
    - 將腳本保存為 `move_files.py`。
    - 使用Python解釋器運行腳本，並在提示時提供源目錄路徑。

3. **運行腳本的命令**：
    ```shell
    python move_files.py
    ```

4. **輸入源目錄**：在提示時，輸入包含需要移動內容的子目錄的完整路徑。

### 示例

```shell
Enter the source directory: /path/to/your/source/directory
Starting to process the source directory: /path/to/your/source/directory
...
文件移動完成!
```



---
