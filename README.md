## Move Files to Parent 
移動文件到父目錄

### Description 描述

The `move-files-to-parent` script is designed to move all contents (files and directories) from subdirectories to their parent directory. `move-files-to-parent` 腳本旨在將所有內容（文件和目錄）從子目錄移動到其父目錄。

It also removes any empty subdirectories after the contents have been moved. 移動內容後，它還會刪除任何空的子目錄。

This script is useful for organizing files by consolidating all items from nested directories into a single parent directory. 此腳本有助於通過將嵌套目錄中的所有項目集中到一個父目錄中來組織文件。

### Features 功能

- **Move Files**: Automatically move all files from subdirectories to the specified parent directory. **移動文件**：自動將所有文件從子目錄移動到指定的父目錄。
- **Move Directories**: Move entire directories from subdirectories to the parent directory if they do not already exist in the parent directory. **移動目錄**：將整個目錄從子目錄移動到父目錄（如果目標目錄中不存在）。
- **Cleanup**: Remove any empty subdirectories after moving their contents. **清理**：在移動內容後刪除任何空的子目錄。

### Requirements 要求

- Python 3.x
- 對源目錄具有讀寫權限

### Usage 使用方法

1. **Prepare the Environment**: Ensure you have Python 3 installed on your system. 安裝任何必要的依賴項。
2. **Edit and Run the Script**: Save the script as `move_files.py`. 編輯並運行腳本，將其保存為 `move_files.py`。
3. **Command to Run the Script**: Use the following command to run the script. 使用以下命令運行腳本：
    ```shell
    python move_files.py
    ```
4. **Input Source Directory**: When prompted, enter the full path to the directory containing subdirectories whose contents need to be moved. 輸入源目錄：在提示時，輸入包含需要移動內容的子目錄的完整路徑。

### Example 示例

```shell
Enter the source directory: /path/to/your/source/directory
Starting to process the source directory: /path/to/your/source/directory
...
文件移動完成!
```

