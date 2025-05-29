from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("********************MENU********************")
    print("** 1. Them sinh vien.                    **")
    print("** 2. Cap nhat thong tin sinh vien boi ID. **")
    print("** 3. Xoa sinh vien boi ID.              **")
    print("** 4. Tim kiem sinh vien theo ten.       **")
    print("** 5. Sap xep sinh vien theo diem trung binh. **")
    print("** 6. Sap xep sinh vien theo ten chuyen nganh. **")
    print("** 7. Hien thi danh sach sinh vien.      **")
    print("** 0. Thoat                              **")
    print("********************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")

elif (key == 2):
    if (qlsv.soLuongSinhVien() > 0):
        print("\nn2. Cap nhat thong tin sinh vien. ")
        print("\nNhap ID: ")
        ID = int(input())
        qlsv.updateSinhVien(ID)
    else:
        print("\nSanh sach sinh vien trong!")
elif (key == 3):
    if (qlsv.soLuongSinhVien() > 0):
        print("\nn3. Xoa sinh vien.")
        print("\nNhap ID: ")
        ID = int(input())
        if (qlsv.deleteById(ID)):
            print("\nnSinh vien co id = ", ID, " da bi xoa.")
        else:
            print("\nnSinh vien co id = ", ID, " khong ton tai.")
    else:
        print("\nnSanh sach sinh vien trong!")
elif (key == 4):
    if (qlsv.soLuongSinhVien() > 0):
        print("\nn4. Tim kiem sinh vien theo ten.")
        print("\nNhap ten de tim kiem: ")
        name = input()
        searchResult = qlsv.findByName(name)
        qlsv.showSinhVien(searchResult)
    else:
        print("\nnSanh sach sinh vien trong!")
elif (key == 5):
    if (qlsv.soLuongSinhVien() > 0):
        print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
        qlsv.sortByDiemTB()
        qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
        print("\nnSanh sach sinh vien trong!")
elif (key == 6):
    if (qlsv.soLuongSinhVien() > 0):
        print("\nn6. Sap xep sinh vien theo ten.")
        qlsv.sortByName()
        qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
        print("\nnSanh sach sinh vien trong!")
elif (key == 7):
    if (qlsv.soLuongSinhVien() > 0):
        print("\nn7. Hien thi danh sach sinh vien.")
        qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
        print("\nnSanh sach sinh vien trong!")
elif (key == 0):
    print("\nBan da chon thoat chuong trinh!")
    break
else:
    print("\nKhong co chuc nang nay!")
    print("\nHãy chon chuc nang trong hop menu.")