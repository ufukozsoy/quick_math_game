import random
import time

def quick_math_game():
    score = 0
    total_questions = 5
    time_limit = 30  # Saniye cinsinden süre
    start_time = time.time()

    print("Hızlı Matematik Oyununa Hoşgeldiniz!")
    print(f"{total_questions} soruya cevap vermek için {time_limit} saniyeniz var.")
    print("Başlamak için Enter'a basın...")
    input()

    for _ in range(total_questions):
        if time.time() - start_time > time_limit:
            print("Süre doldu!")
            break

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2

        try:
            player_answer = int(input(f"{num1} + {num2} = ? "))
            if player_answer == correct_answer:
                print("Doğru cevap! Puan kazandınız.")
                score += 1
            else:
                print(f"Yanlış cevap! Doğru cevap: {correct_answer}")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    print(f"Oyun bitti! Toplam puanınız: {score}")

if __name__ == "__main__":
    quick_math_game()

