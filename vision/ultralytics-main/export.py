from ultralytics import YOLO

def export_model():
    # 加载训练好的模型
    model = YOLO('C:/Users/17850/Desktop/ultralytics-main/runs/train/exp/weights/best.pt')

    # 导出模型为 ONNX 格式
    results = model.export(format='onnx', imgsz=224)

    if results:
        print("模型成功导出为 ONNX 格式。")
    else:
        print("模型导出失败。")

if __name__ == "__main__":
    export_model()