# 중간고사 준비와 실습 경험

## 탬플릿 4종의 구조.
1. snake.py
- 리스트의 첫 번째 요소 -> 'snake[0]' 뱀의 머리. / 리스트의 나머지 요소 -> 뱀의 몸통.
- 매 프레임마다, 리스트의 맨 앞에 새로운 머리_'head'를 추가_'insert' 하고, 먹이를 섭취하지 않았다면 꼬리 끝을 제거_'pop' 한다.
- 머리 좌표가 'WIDTH', 'HEIGHT'의 범위를 벗어나거나, 머리_'head'가 리스트에 있는지 확인된다면_'head in snake' 'game_over_screen'을 띄운다.
- 'new_food' 함수로 격자 내의 아무 공간에 무작위로 생성된다. 'if pos not in snake'로 먹이가 뱀의 몸통에 생성되지 않도록 한다.
- 그리드 기반 시스템으로, 화면 전체를 'CELL' 단위로 나누어 생각한다. 뱀도 'CELL'만큼 움직이고, 먹이의 생성 위치도 'CELL'의 배수로 설정된다.
2. dodger.py
- 
3. breakout.py
- 
4. space_shooter
- 

##
