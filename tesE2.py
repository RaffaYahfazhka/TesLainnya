def selisih_maksimal(arr):
    if len(arr) < 2:
        return None  # Jika array memiliki kurang dari dua elemen, tidak ada selisih yang bisa dihitung

    maksimal_selisih = arr[1] - arr[0]
    minimal_elemen = arr[0]

    for harga in arr[1:]:
        selisih = harga - minimal_elemen
        maksimal_selisih = max(maksimal_selisih, selisih)
        minimal_elemen = min(minimal_elemen, harga)

    return maksimal_selisih

# Contoh pemanggilan fungsi
harga = [10, 7, 5, 8, 11, 9, 1]
hasil = selisih_maksimal(harga)
print(hasil)  
