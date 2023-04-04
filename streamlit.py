import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

# menampilkan teks pada tampilan Streamlit
st.title(("Clustering Analysis of Pokemon's Ability Status"))

df = pd.read_csv('output.csv', sep=';')

result = pd.read_csv('result.csv', sep=',')

# buat list berisi path dari gambar yang akan ditampilkan
df['gambar'] = [('img/'+i) for i in df['gambar']]

options = {
    0: 'Cluster 1',
    1: 'Cluster 2',
    2: 'Cluster 3',
    3: 'Cluster 4',
    4: 'Cluster 5',
    5: 'Cluster 6'
}
st.write("---")
option = st.select_slider(
    "**Select Number of Clusters**",
    (0, 1, 2, 3, 4, 5),
    format_func=lambda x: options[x]
)
st.write("---")

df = df[df['label'] == option]

if st.button('Detail'):
    # Fungsi untuk menampilkan gambar
    def display_image(image_path):
        with open(image_path, "rb") as f:
            image = f.read()
        return st.image(image, width=100)

    # Tampilkan tabel dan gambar
    for index, row in df.iterrows():
        with st.container():
            st.write(f'**{row["main_name"]}**')
            st.write(
                f'HP : {row["hp"]} | Attack : {row["attack"]} | Defense : {row["defense"]} | SpAtk : {row["spatk"]} | SpDef : {row["spdef"]} | Speed : {row["speed"]}')
        st.write("Image : ")
        display_image(row["gambar"])
        st.write("---")

elif st.button('Summary'):
    st.table(result)

else:
    # tentukan jumlah kolom pada grid
    num_cols = 9

    image_paths = df['gambar'].values

    main_name = df['main_name'].values

    # hitung jumlah baris yang diperlukan
    num_rows = int(np.ceil(len(image_paths) / num_cols))

    # buat kolom untuk menampilkan gambar dalam grid
    cols = st.columns(num_cols)

    # loop untuk menampilkan gambar pada setiap cell pada grid
    for i, path in enumerate(image_paths):
        with cols[i % num_cols]:
            image = Image.open(path)
            st.image(image, use_column_width=True, caption=f"{main_name[i]}")


# # menambahkan kolom untuk menampilkan gambar
# df["image_display"] = df["gambar"].apply(lambda x: st.image(x, width=50))

# # menampilkan data frame dan menghilangkan kolom "image"
# st.table(df.drop("gambar", axis=1))

# # menampilkan tabel dengan gambar
# for i, row in df.iterrows():
#     st.write(row["hp"], row["attack"],row["attack"],row["defense"],row["spatk"],row["spdef"],row["speed"],row["main_name"])
#     st.image(row["gambar"], width=100)


# # membuat fungsi untuk menampilkan gambar dengan ukuran yang ditentukan
# def image_resize(image_paths, size):
#     img = Image.open(image_paths)
#     img = img.resize(size)
#     return img

# # menampilkan tabel dengan gambar di dalamnya
# st.write("## Data with Images")
# for index, row in df.iterrows():
#     # membuat tag HTML untuk menampilkan gambar dalam tabel
#     img_tag = f'<img src="{image_paths[index]}">'
#     # menampilkan tabel dengan kolom gambar sebagai HTML
#     st.table({
#         "Name": [row["speed"]],
#         "Age": [row["attack"]],
#         "Image": [img_tag]
#     })
