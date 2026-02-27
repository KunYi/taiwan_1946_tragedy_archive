import os
from PIL import Image

def generate_grid(rows, cols_per_row):
    """根據你的特殊規律生成索引矩陣"""
    grid = []
    for r in range(rows):
        row_indices = []
        group_r = r // 3
        sub_r = r % 3
        base_start = group_r * 39

        # 前 12 欄 (4 個 3x3 區塊)
        for block in range(4):
            block_start = base_start + (block * 9) + (sub_r * 3)
            row_indices.extend([block_start, block_start + 1, block_start + 2])

        # 第 13 欄
        last_col_idx = base_start + 36 + sub_r
        row_indices.append(last_col_idx)
        grid.append(row_indices)
    return grid

def stitch_by_folder(folder_path, output_path):
    """針對單一資料夾進行拼接"""
    cols_per_row = 13
    rows = 18
    grid = generate_grid(rows, cols_per_row)

    # 檢查第一張圖是否存在以獲取基礎路徑格式
    test_path = os.path.join(folder_path, "tile_000.jpg")
    if not os.path.exists(test_path):
        print(f"跳過 {folder_path}: 找不到 tile_000.jpg")
        return

    # 計算尺寸
    col_widths = []
    for c in range(cols_per_row):
        with Image.open(os.path.join(folder_path, f"tile_{grid[0][c]:03d}.jpg")) as img:
            col_widths.append(img.width)

    row_heights = []
    for r in range(rows):
        with Image.open(os.path.join(folder_path, f"tile_{grid[r][0]:03d}.jpg")) as img:
            row_heights.append(img.height)

    # 建立畫布
    canvas = Image.new('RGB', (sum(col_widths), sum(row_heights)))

    current_y = 0
    for r in range(rows):
        current_x = 0
        for c in range(cols_per_row):
            img_idx = grid[r][c]
            path = os.path.join(folder_path, f"tile_{img_idx:03d}.jpg")
            if os.path.exists(path):
                with Image.open(path) as img:
                    canvas.paste(img, (current_x, current_y))
            current_x += col_widths[c]
        current_y += row_heights[r]

    canvas.save(output_path, quality=95)
    print(f"已完成: {output_path} ({canvas.width}x{canvas.height})")

def main():
    # 設定輸入與輸出目錄
    raw_data_dir = "raw_data"
    output_dir = "processed_images"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 自動掃描 raw_data 下的所有子目錄 (例如 April15, April16...)
    if not os.path.exists(raw_data_dir):
        print(f"錯誤: 找不到 {raw_data_dir} 目錄")
        return

    folders = [f for f in os.listdir(raw_data_dir) if os.path.isdir(os.path.join(raw_data_dir, f))]

    for folder in folders:
        input_folder = os.path.join(raw_data_dir, folder)
        output_file = os.path.join(output_dir, f"{folder}_stitched.jpg")
        stitch_by_folder(input_folder, output_file)

if __name__ == "__main__":
    main()
