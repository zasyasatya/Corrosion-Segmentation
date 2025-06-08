import os
import cv2
import glob
import subprocess

MODEL_PATH = "pretrained/HRNet_var/21-12-28[17.09]"
N_MC = 24
OUT_RES = [512, 512]
THRESH = 0.75
input_path = "testing_images/"  # bisa folder gambar atau file video

def run_infer(image_path):
    cmd = [
        "python", "var_infer.py",
        "--model", MODEL_PATH,
        "--n_MC", str(N_MC),
        "--out_res", str(OUT_RES[0]), str(OUT_RES[1]),
        "--thresh", str(THRESH),
        "--image", image_path
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

def process_image_folder(folder):
    images = sorted(glob.glob(folder))
    print(images)
    # Ambil hanya frame kelipatan 5 (misal: frame_00005.jpg, dst)
    # selected = [img for img in images if int(os.path.splitext(os.path.basename(img))[0].split('_')[-1]) % 5 == 0]
    for img in images:
        run_infer(img)

def process_video(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video FPS: {fps}, Total frames: {frame_count}")
    frame_idx = 0
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Ambil 5 frame per detik, hanya frame ke-0, 5, 10, dst per detik
        if int(frame_idx % fps) % 5 == 0:
            out_path = os.path.join(output_folder, f"frame_{frame_idx:05d}.jpg")
            cv2.imwrite(out_path, frame)
            run_infer(out_path)
            saved += 1
        frame_idx += 1
    cap.release()
    print(f"Total frames processed: {saved}")

if __name__ == "__main__":
    # Ganti path di bawah sesuai kebutuhan
    if os.path.isdir(input_path):
        process_image_folder(input_path)
    elif input_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        process_video(input_path, "extracted_frames")
    else:
        print("Input path tidak dikenali.")