import torch
from torchvision import transforms
from PIL import Image
from model import DigitModel

def load_model(model_path="digit_model.pth"):
    model = DigitModel()
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    img = Image.open(image_path)
    return transform(img).unsqueeze(0)

def predict_digit(image_path, model_path="digit_model.pth"):
    model = load_model(model_path)
    img_tensor = preprocess_image(image_path)
    with torch.no_grad():
        output = model(img_tensor)
        predicted = torch.argmax(output, dim=1).item()
    return predicted

if __name__ == "__main__":
    test_image = "sample_digit.png"  # Replace with your image
    prediction = predict_digit(test_image)
    print(f"Predicted Digit: {prediction}")
