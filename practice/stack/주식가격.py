# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# 입출력 예
# prices	         return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.


#처음에 내가 생각한 풀이
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        if i + 1 != len(prices): #인덱스가 마지막 요소를 가리키고 있지 않다면
            for j in range(i + 1,len(prices)): #현재 요소를 제외한 나머지 주식 가격을 끝까지 비교하기 위한 순회
                cnt += 1 #다음 주식 가격으로 이동하면서 1초가 지났으므로 무조건 더해줌 
                if prices[i] > prices[j]: #이후 주식 가격이 떨어진 경우
                    break #순회 중단
        answer.append(cnt)
    return answer



#스택을 이용한 풀이 
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]: #스택이 비어있지 않은 경우 스택에 제일 마지막에 있는 주식 가격(이전 시점에서 매수했을 때 주식가)과 현재 주식 가격을 비교하여 매수했을 때보다 현재 주식 가격이 낮으면 주식이 떨어진 것 
                past, _ = stack.pop() #매수시점을 past에 담아놓고
                answer[past] = i - past #현재시점에서 매수 시점을 빼준 값이 가격이 떨어지지 않은 기간
                #무한 루프이기 때문에 현재가격보다 매수가격이 더 높은 경우 다 pop됨 
        stack.append([i, prices[i]])
    for i, _ in stack: #스택에 남아있는 배열은 
        answer[i] = len(prices) - 1 - i #끝까지 가격이 안떨어진 경우임
    return answer