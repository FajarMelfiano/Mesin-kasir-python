import sys
import os

PRODUCTS = {
    1: {"name": "Downy", "price": 23000},
    2: {"name": "Baygon", "price": 41100},
    3: {"name": "Mamy Poko", "price": 59000},
    4: {"name": "Ovaltine", "price": 23000},
    5: {"name": "Beras", "price": 70000},
    6: {"name": "Indomie", "price": 3000},
    7: {"name": "Kecap", "price": 12000},
    8: {"name": "Saos", "price": 10000},
    9: {"name": "Masako", "price": 500},
    10: {"name": "Gula", "price": 15000},
    11: {"name": "Garam", "price": 10000},
    12: {"name": "Mie", "price": 1000},
    13: {"name": "Telur", "price": 20000},
    14: {"name": "Susu", "price": 15000},
    15: {"name": "Kopi", "price": 10000},
    16: {"name": "Teh", "price": 5000},
    17: {"name": "Cokelat", "price": 25000},
    18: {"name": "Kue", "price": 10000},
    19: {"name": "Roti", "price": 5000},
    20: {"name": "Susu Kental Manis", "price": 12000},
    21: {"name": "Krimer", "price": 15000},
    22: {"name": "Mentega", "price": 20000},
    23: {"name": "Krim", "price": 30000},
    24: {"name": "Kopi Sosro", "price": 10000},
    25: {"name": "Teh Kotak", "price": 5000},
    26: {"name": "Kopi Torabika", "price": 10000},
}

def print_header():
    print("-" * 30)
    print("KASIR AA")
    print("-" * 30)

def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

def display_products():
    print(" No | Nama Barang    | Harga")
    print("-" * 45)
    for code, product in PRODUCTS.items():
        print(f" {code:<2} | {product['name']:<13} | {format_rupiah(product['price'])}")
    print("-" * 45)

def get_product_input():
    while True:
        try:
            code = int(input("Masukkan angka barang  : "))
            if code not in PRODUCTS:
                raise ValueError
            quantity = int(input("Masukkan jumlah barang : "))
            return code, quantity
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

def calculate_total(purchases):
    return sum(PRODUCTS[code]["price"] * quantity for code, quantity in purchases)

def calculate_discount(total):
    if total > 500000:
        return total * 0.08
    elif total > 300000:
        return total * 0.05
    elif total > 200000:
        return total * 0.03
    elif total > 100000:
        return total * 0.01
    return 0

def process_payment(total):
    while True:
        try:
            payment = int(input("Bayar            : "))
            if payment < total:
                print("Pembayaran kurang. Silakan coba lagi.")
                continue
            return payment
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_receipt(purchases, subtotal, discount, total, payment, change):
    clear_screen()
    print_header()
    print("\n" + "=" * 40)
    print("              STRUK BELANJA            ")
    print("=" * 40)
    print("Barang yang dibeli:")
    for code, quantity in purchases:
        product = PRODUCTS[code]
        print(f"{product['name']:<15} x {quantity:<3} {format_rupiah(product['price'] * quantity):>15}")
    print("-" * 40)
    print(f"SubTotal         : {format_rupiah(subtotal):>15}")
    print(f"Potongan Harga   : {format_rupiah(discount):>15}")
    print(f"Total            : {format_rupiah(total):>15}")
    print(f"Pembayaran       : {format_rupiah(payment):>15}")
    print(f"Kembalian        : {format_rupiah(change):>15}")
    print("=" * 40)
    print("          Terima Kasih         ")
    print("=" * 40)

def main():
    purchases = []

    while True:
        clear_screen()
        print_header()
        display_products()
        code, quantity = get_product_input()
        purchases.append((code, quantity))

        if input("\nIngin tambah barang? [y/t] : ").lower() != 'y':
            break

    subtotal = calculate_total(purchases)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    clear_screen()
    print_header()
    print("\n" + "-" * 40)
    print(f"SubTotal         : {format_rupiah(subtotal)}")
    print(f"Potongan Harga   : {format_rupiah(discount)}")
    print(f"Total            : {format_rupiah(total)}")
    print("-" * 40)

    payment = process_payment(total)
    change = payment - total

    print_receipt(purchases, subtotal, discount, total, payment, change)

if __name__ == "__main__":
    main()