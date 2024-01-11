import random

correct_answer=random.randint(1,10)
while (1):
  user_answer=int(input("숫자를 맞춰보세요."))
  if user_answer==correct_answer:
    print(f"맞췄습니다. 정답은 {correct_answer}입니다")
    break
  else: print("땡!")