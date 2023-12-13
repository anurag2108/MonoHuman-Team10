import streamlit as st

st.title('MonoHuman')

st.image('assets/teaser.jpg')

st.markdown('''MonoHuman - which robustly renders view-consistent and high-fidelity avatars under arbitrary novel poses.
         Our key insight is to model the deformation field with bi-directional constraints and explicitly leverage the 
        off-the-peg keyframe information to reason the feature correlations for coherent results. In particular, we first propose a Shared Bidirectional Deformation module, which creates a pose-independent 
        generalizable deformation field by disentangling backward and forward deformation correspondences into shared 
        skeletal motion weight and separate non-rigid motions. Then, we devise a Forward Correspondence Search module,which queries the correspondence feature of keyframes 
        to guide the rendering network. The rendered results are thus multi-view consistent with high fidelity, 
        even under challenging novel pose settings. Extensive experiments demonstrate the superiority of proposed 
        MonoHuman over state-of-the-art methods.''')

st.title('Architecture:')

st.image('assets/arcitecture.png')

st.title('Steps to execute our model:')

st.markdown('''
To execute MonoHuman successfully and resolve any errors, we have followed the steps outlined below:  
            1) Clear the chumpy objects from SMPL model and upload SMPL model in third_parties/smpl/models present in the monohuman repository.  
            2)Change data path in tools/prepare_zju_mocap/377 to ../  
            3)Extract CoreView_377.tar.gz in /content/MonoHuman/tools.  
            4)Prepare xxx datafile using the command – !python prepare_dataset.py --cfg xxx.yaml.  
5)Once extracted we move all the files present in folder 0 to its parent folder.  
6)In core/nets/monohuman/network.py, we change line line 81 and 60 and add .to('cpu') to the index to remove GPU related errors.  
7)We then finally train the model for 6-8 hours using the command -  
        !python train.py --cfg configs/monohuman/zju_mocap/377/377.yaml resume False   
8)Once the experiments folder is generated for the model trained weights, we run the inference using-   
        !python run.py --type movement --cfg configs/monohuman/zju_mocap/377/377.yaml   ''')

st.title('Milestones:')

st.markdown('''
To execute MonoHuman successfully and resolve any errors, we have followed the steps outlined below:  
            1) Clear the chumpy objects from SMPL model and upload SMPL model in third_parties/smpl/models present in the monohuman repository.  
            2)Change data path in tools/prepare_zju_mocap/377 to ../  
            3)Extract CoreView_377.tar.gz in /content/MonoHuman/tools.  
            4)Prepare xxx datafile using the command – !python prepare_dataset.py --cfg xxx.yaml.  
5)Once extracted we move all the files present in folder 0 to its parent folder.  
6)In core/nets/monohuman/network.py, we change line line 81 and 60 and add .to('cpu') to the index to remove GPU related errors.  
7)We then finally train the model for 6-8 hours using the command -  
        !python train.py --cfg configs/monohuman/zju_mocap/377/377.yaml resume False   
8)Once the experiments folder is generated for the model trained weights, we run the inference using-   
        !python run.py --type movement --cfg configs/monohuman/zju_mocap/377/377.yaml   ''')

st.title('Code Trace of MonoHuman:')

st.image('assets/MonoHuman_Train.png', caption='Code trace of MonoHuman')

st.title('Results generated after 8 hours Training:')

video_file = open('assets/generated-results-377.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)