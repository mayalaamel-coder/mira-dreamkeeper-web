import edge_tts
import asyncio
import os
import shutil

# Daftar Dialog lengkap 70 baris
dialogs = [
    [span_0](start_span)[span_1](start_span)("Aris", "Halo semuanya, selamat datang di episode khusus A-P-B-D Unlocked. Hari ini kita bakal bedah dokumen riset tentang gimana teknologi digital pernah nyelametin duit warga Jakarta triliunan rupiah.[span_0](end_span)[span_1](end_span)"),
    [span_2](start_span)("Geo", "Spill the tea, Ris! Gue denger ini soal drama paling legendaris antara Ahok sama D-P-R-D pas zaman itu kan?[span_2](end_span)"),
    [span_3](start_span)[span_4](start_span)("Aris", "Tepat banget. Kita bakal bahas E-Budgeting. Tapi sebelum masuk ke sana, kita harus tahu dulu betapa sus atau mencurigakannya sistem manual zaman dulu.[span_3](end_span)[span_4](end_span)"),
    [span_5](start_span)("Geo", "Duh, kalau denger kata manual di birokrasi, pikiran gue langsung ke arah korupsi, pungli, sama tumpukan kertas yang berdebu.[span_5](end_span)"),
    [span_6](start_span)[span_7](start_span)("Aris", "Gak salah sih. Riset ini nyebutin kalau dulu, proses anggaran itu gelap banget. Masyarakat nggak bisa akses drafnya, dan semuanya serba tertutup.[span_6](end_span)[span_7](end_span)"),
    [span_8](start_span)("Geo", "Bau-bau konspirasi ya? Berarti dulu nggak ada yang tahu duit pajak kita lari ke mana sebelum anggarannya diketok palu?[span_8](end_span)"),
    [span_9](start_span)[span_10](start_span)("Aris", "Gak ada. Titik paling kritisnya itu pas tahap re-typing atau pengetikan ulang dokumen setelah rapat. Di situ tangan gaib mulai main.[span_9](end_span)[span_10](end_span)"),
    [span_11](start_span)[span_12](start_span)("Geo", "Bentar, pengetikan ulang? Jadi setelah dibilang Deal, dokumennya diketik lagi secara manual? Itu mah celah banget buat ganti angka[span_11](end_span)[span_12](end_span)!"),
    [span_13](start_span)[span_14](start_span)("Aris", "Exactly. Makanya muncul istilah Anggaran Siluman. Program yang nggak pernah dibahas di rapat, tiba-tiba muncul pas dokumennya mau dicetak.[span_13](end_span)[span_14](end_span)"),
    [span_15](start_span)("Geo", "Red flag parah sih itu. Terus, pas Ahok masuk, dia langsung ganti ke digital kan?[span_15](end_span)"),
    [span_16](start_span)[span_17](start_span)("Aris", "Iya, lewat Pergub Nomor seratus empat puluh lima Tahun dua ribu tiga belas. Dia ngenalin E-Budgeting yang punya fitur Digital Audit Trail.[span_16](end_span)[span_17](end_span)"),
    [span_18](start_span)("Geo", "Audit trail? Bahasa manusianya apa tuh, Ris?[span_18](end_span)"),
    [span_19](start_span)("Aris", "Singkatnya, setiap orang yang login dan ganti angka di sistem, namanya kecatat. Jam berapa dia ngubah, apa yang diubah, semuanya ada jejak digitalnya.[span_19](end_span)"),
    [span_20](start_span)("Geo", "Jadi nggak bisa lagi ya pakai jurus Saya nggak tahu, itu kesalahan staf? Kelihatan dong siapa yang nakal.[span_20](end_span)"),
    [span_21](start_span)("Aris", "Nggak bisa. Dan ada lagi yang namanya System Lock. Begitu anggaran disetujui, sistem otomatis ngunci datanya.[span_21](end_span)"),
    [span_22](start_span)("Geo", "Berarti kalau sudah deal, datanya nggak bisa diedit lagi di luar sistem?[span_22](end_span)"),
    [span_23](start_span)("Aris", "Iya. Begitu disetujui melalui alur digital, datanya terkunci otomatis. Ini menghilangkan modus penyisipan program pasca-sidang paripurna.[span_23](end_span)"),
    [span_24](start_span)("Geo", "Berarti legitimasi anggaran pindah dari paraf fisik ke validasi digital berbasis akun ya, Ris?[span_24](end_span)"),
    [span_25](start_span)("Aris", "Tepat! Dan yang paling berpengaruh buat kita adalah Transparansi Pra-Legislasi.[span_25](end_span)"),
    [span_26](start_span)("Geo", "Itu maksudnya masyarakat bisa lihat drafnya sebelum jadi hukum?[span_26](end_span)"),
    [span_27](start_span)[span_28](start_span)("Aris", "Betul. Versi awal R-A-P-B-D dan K-U-A P-P-A-S dipublikasikan di situs resmi agar bisa diakses siapa saja.[span_27](end_span)[span_28](end_span)"),
    [span_29](start_span)("Geo", "Wah, jadi netizen bisa langsung geruduk kalau ada alokasi yang nggak masuk akal sejak tahap perencanaan?[span_29](end_span)"),
    [span_30](start_span)("Aris", "Pernah kejadian kok. Publik memprotes anggaran revitalisasi kolam air mancur D-P-R-D senilai ratusan juta yang akhirnya dicoret.[span_30](end_span)"),
    [span_31](start_span)("Geo", "Power of Netizen emang nggak ada obat kalau dikasih data transparan[span_31](end_span)!"),
    [span_32](start_span)[span_33](start_span)("Aris", "Tapi sistem ini dapet ujian berat tahun dua ribu lima belas, yaitu insiden Anggaran Siluman dua belas koma satu Triliun.[span_32](end_span)[span_33](end_span)"),
    [span_34](start_span)("Geo", "Itu angka yang gede banget! Gimana kronologinya sampai bisa ketahuan?[span_34](end_span)"),
    [span_35](start_span)("Aris", "Padahal tanggal dua puluh tujuh Januari dua ribu lima belas, Pemprov dan D-P-R-D sudah setuju A-P-B-D tujuh puluh tiga koma nol delapan triliun.[span_35](end_span)"),
    [span_36](start_span)("Geo", "Tapi setelah itu ada yang main belakang lagi?[span_36](end_span)"),
    [span_37](start_span)("Aris", "Iya. Di bulan Februari, Ahok mengungkap ada dana dua belas koma satu triliun yang disisipkan secara diam-diam oleh D-P-R-D.[span_37](end_span)"),
    [span_38](start_span)("Geo", "Gimana caranya Ahok bisa seyakin itu kalau ada penyisipan sebesar itu?[span_38](end_span)"),
    [span_39](start_span)("Aris", "Karena dia cek di sistem E-Budgeting-nya. Dia nemu perbedaan antara dokumen cetak D-P-R-D dengan versi digital yang sudah terkunci.[span_39](end_span)"),
    [span_40](start_span)("Geo", "Jadi E-Budgeting berhasil jadi alat deteksi meskipun penyisipan itu tetap dicoba?[span_40](end_span)"),
    [span_41](start_span)("Aris", "Betul. Salah satu item yang viral adalah pengadaan U-P-S senilai empat koma dua miliar untuk kelurahan.[span_41](end_span)"),
    [span_42](start_span)("Geo", "Sarkastik banget. Empat miliar buat satu U-P-S? Itu kelurahan apa pusat data n-a-s-a?[span_42](end_span)"),
    [span_43](start_span)[span_44](start_span)("Aris", "Itulah sebabnya Ahok menolak versi D-P-R-D dan mengirim versi E-Budgeting yang benar ke Kemendagri.[span_43](end_span)[span_44](end_span)"),
    [span_45](start_span)("Geo", "Terus D-P-R-D pasti nggak terima dong kekuasaannya dipangkas teknologi?[span_45](end_span)"),
    [span_46](start_span)("Aris", "Parah. Mereka menolak dokumen elektronik itu karena nggak ada tanda tangan fisik. Mereka akhirnya pakai Hak Angket.[span_46](end_span)"),
    [span_47](start_span)[span_48](start_span)("Geo", "Jadi konflik ini bukan cuma soal duit, tapi soal siapa yang lebih berkuasa: Tanda tangan pejabat atau Sistem Digital?[span_47](end_span)[span_48](end_span)"),
    [span_49](start_span)[span_50](start_span)("Aris", "Tepat. Kasus ini bahkan sampai ke ranah hukum. Ahok melaporkan temuan bukti digital ini ke K-P-K.[span_49](end_span)[span_50](end_span)"),
    [span_51](start_span)("Geo", "Bukti digital dari E-Budgeting itu bisa dianggap sah secara hukum nggak sih?[span_51](end_span)"),
    [span_52](start_span)("Aris", "Ahok menjadikannya fondasi utama untuk identifikasi manipulasi. Sistem ini jadi alat forensik digital.[span_52](end_span)"),
    [span_53](start_span)("Geo", "Terus gimana respon D-P-R-D pas dituduh gitu?[span_53](end_span)"),
    [span_54](start_span)("Aris", "Mereka lapor balik Pemprov ke K-P-K dan Bareskrim, nuduh ada suap dan korupsi dua belas koma tujuh triliun.[span_54](end_span)"),
    [span_55](start_span)("Geo", "Nuduh balik? Dasar buktinya apa?[span_55](end_span)"),
    [span_56](start_span)("Aris", "Mereka pakai dokumen versi mereka yang isinya juga aneh, kayak anggaran trilogi buku Ahok senilai tiga puluh miliar.[span_56](end_span)"),
    [span_57](start_span)("Geo", "Jadi ada dua versi anggaran yang beroperasi paralel ya? Satu yang bener, satu yang ajaib.[span_57](end_span)"),
    [span_58](start_span)("Aris", "Itulah kenapa B-P-K juga ikut mantau, meskipun mereka baru bisa audit setelah A-P-B-D disahkan.[span_58](end_span)"),
    [span_59](start_span)("Geo", "Berarti ada celah waktu di mana pengawasan eksternal belum berlaku, dan di situlah E-Budgeting jadi penjaga gawang.[span_59](end_span)"),
    [span_60](start_span)("Aris", "Benar. Keandalan sistem ini bukan cuma soal siapa yang dipenjara, tapi kemampuannya menghasilkan bukti yang solid.[span_60](end_span)"),
    [span_61](start_span)("Geo", "Jadi, apa warisan atau legacy jangka panjang dari sistem ini buat Jakarta?[span_61](end_span)"),
    [span_62](start_span)[span_63](start_span)("Aris", "Pertama, standar baru transparansi. Platform ini jadi model nasional yang bahkan dipuji Presiden Jokowi.[span_62](end_span)[span_63](end_span)"),
    [span_64](start_span)("Geo", "Wah, dari Jakarta untuk Indonesia ya?[span_64](end_span)"),
    [span_65](start_span)("Aris", "Iya. Tapi ada catatan penting: sistem ini hanya digital, bukan cerdas.[span_65](end_span)"),
    [span_66](start_span)("Geo", "Maksudnya bukan cerdas itu gimana? Nggak ada a-i-nya?[span_66](end_span)"),
    [span_67](start_span)("Aris", "Belum ada validasi otomatis. Misalnya, kalau ada yang input harga Lem Aibon delapan puluh dua miliar, sistem nggak langsung nolak.[span_67](end_span)"),
    [span_68](start_span)("Geo", "Jadi tetap butuh manusia yang jujur dan teliti buat input datanya?[span_68](end_span)"),
    [span_69](start_span)("Aris", "Betul. Keandalan E-Budgeting itu pada kemampuannya merekam setiap tindakan agar tidak bisa disembunyikan.[span_69](end_span)"),
    [span_70](start_span)("Geo", "Pelajaran buat kita, teknologi itu cuma alat, tapi alat yang bikin koruptor nggak bisa lagi main di ruang gelap.[span_70](end_span)"),
    [span_71](start_span)[span_72](start_span)("Aris", "Tepat! Itulah kenapa partisipasi publik buat mantau data itu super penting.[span_71](end_span)[span_72](end_span)"),
    [span_73](start_span)("Geo", "Gue ngebayangin orang-orang yang biasanya main belakang pasti panik banget pas sistem ini jalan.[span_73](end_span)"),
    [span_74](start_span)[span_75](start_span)("Aris", "Panik parah! Kasus dua ribu lima belas itu jadi bukti operasional pertama tentang keandalan E-Budgeting.[span_74](end_span)[span_75](end_span)"),
    [span_76](start_span)("Geo", "Pelajaran buat Gen Z, jangan cuma jago scroll sosmed, sesekali scroll draf A-P-B-D daerah masing-masing.[span_76](end_span)"),
    [span_77](start_span)[span_78](start_span)("Aris", "Benar. Setiap intervensi ilegal sekarang meninggalkan jejak digital yang tak terhapus. Itu senjata kita.[span_77](end_span)[span_78](end_span)"),
    [span_79](start_span)[span_80](start_span)("Geo", "Makasih banyak Aris buat bedah risetnya. Gue jadi makin paham kalau teknologi itu kunci lawan korupsi.[span_79](end_span)[span_80](end_span)"),
    [span_81](start_span)("Aris", "Sama-sama, Geo. Seneng bisa sharing hal yang edukatif tapi tetep asik.[span_81](end_span)"),
    ("Geo", "Jadi kesimpulannya, E-Budgeting itu bikin korupsi jadi High Risk, Low Reward ya?"),
    [span_82](start_span)[span_83](start_span)("Aris", "Bagus banget bahasanya! Risiko ketahuannya tinggi, tapi hasil curiannya susah disembunyiin.[span_82](end_span)[span_83](end_span)"),
    ("Geo", "Oke guys, sampai sini dulu podcast kita. Jangan lupa cek draf anggaran daerah kalian!"),
    ("Aris", "Sampai jumpa di episode selanjutnya. Stay digital, stay honest!"),
    ("Geo", "Bye-bye semuanya! See ya!"),
]

async def main():
    if not os.path.exists("podcast_output"):
        os.makedirs("podcast_output")
    
    for i, (speaker, text) in enumerate(dialogs):
        voice = "id-ID-ArdiNeural" if speaker == "Aris" else "id-ID-GadisNeural"
        rate = "+10%" if speaker == "Geo" else "+0%"
        output_file = f"podcast_output/{i+1:02d}_{speaker}.mp3"
        
        # Eksekusi TTS
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(output_file)
        print(f"Berhasil: {output_file}")

    # Zip hasil
    shutil.make_archive("hasil_podcast", 'zip', "podcast_output")
    print("\n--- SELESAI! Silakan download hasil_podcast.zip di menu file kiri ---")

# Run proses
await main()
