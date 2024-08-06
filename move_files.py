import os
import shutil

def move_files_to_parent(source_dir):
    for root, dirs, files in os.walk(source_dir, topdown=False):
        print(f"Current directory: {root}")
        if root == source_dir:
            print("Skipping the source directory itself.")
            continue  # 跳過來源目錄本身
        for name in files:
            file_path = os.path.join(root, name)
            parent_dir = source_dir  # 將文件移動到來源目錄
            try:
                print(f"Moving file {file_path} to {parent_dir}")
                shutil.move(file_path, parent_dir)
            except Exception as e:
                print(f"Error moving file {file_path}: {e}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            target_path = os.path.join(source_dir, name)
            try:
                if not os.path.exists(target_path):  # 確保目標目錄不存在
                    print(f"Moving directory {dir_path} to {source_dir}")
                    shutil.move(dir_path, source_dir)
                elif not os.listdir(dir_path):  # 如果子文件夾已空
                    print(f"Removing empty directory {dir_path}")
                    os.rmdir(dir_path)  # 刪除空文件夾
            except Exception as e:
                print(f"Error moving directory {dir_path}: {e}")

source_dir = r'D:\bt\zzzz\nmm-0.12-portable\mods'
print(f"Starting to process the source directory: {source_dir}")
move_files_to_parent(source_dir)
print("文件移動完成!")

# Keep the terminal open to review the output
input("Press Enter to close the terminal window.")
