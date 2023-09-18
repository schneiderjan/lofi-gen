FROM tensorflow/tensorflow:2.11.0-gpu

# Obtain NVIDIA keys
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub 78
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub


RUN apt-get update && apt-get install -y --no-install-recommends  \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgtk2.0-dev \
    libavcodec-dev \
    git

RUN pip install --upgrade pip

RUN pip --no-cache-dir install \
    matplotlib==3.6.3 \
    numpy==1.22.1 \
    opencv-python==4.6.0.66 \
    psutil==5.9.4 \
    scipy==1.8.1 \
    scikit-image==0.19.3 \
    scikit-learn==1.2.1 \
    tensorflow-addons==0.19.0 \
    tensorflow-estimator==2.11.0 \
    tensorflow-hub==0.12.0 \
    tensorflow-io==0.30.0 \
    tensorflow-io-gcs-filesystem==0.30.0 \
    tensorflow-metadata==1.12.0 \
    tensorflow-model-optimization==0.7.3 \
    tensorflow-text==2.11.0 \
    tf-models-official==2.11.3 \
    tf-slim==1.1.0 \