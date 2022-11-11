import argparse

parser = argparse.ArgumentParser(description="사용법 test 입니다") # Parse 객체 생성
parser.add_argument('-p', type=str, help = '-p 안녕하세요' ) # 입력 받고자 하는 옵션 값과 옵션 값 생성
parser.add_argument('-o', type=int, help = '-o 3')

args = parser.parse_args() # 인자들을 파싱하여 args 에 저장

if __name__ =='__main__':
    for i in range(args.o):
        print(args.p)
