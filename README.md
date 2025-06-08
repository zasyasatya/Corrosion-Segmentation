1. Buat Environment dengan Python 3.8.20
2. Install seluruh dependensi dengan perintah > pip install -r requirements.txt
3. Download pretrained model dan extract pada folder "pretrained"
* [HRNet [4.35 GB]](https://drive.google.com/file/d/196yj1ZpuuSn1Uhb8LmKANV0hmnPc2o3F/view?usp=sharing)
* [HRNet_do [487 MB]](https://drive.google.com/file/d/12d6je9A8YOvz_9To3R0MgJzaMUu1UrRZ/view?usp=sharing)
* [HRNet_var [521 MB]](https://drive.google.com/file/d/11GymBbJeyHkq1Td_ThSmGi4AAto20A5z/view?usp=sharing)
4. Jalankan inference pada kode var_infer.py (untuk model HRNet_var). Contoh command:
python var_infer.py --model pretrained/HRNet_var/21-12-28[17.09] --n_MC 24 --out_res 512 512 --thresh 0.75 --image testing_images/DJI_0492.JPG
