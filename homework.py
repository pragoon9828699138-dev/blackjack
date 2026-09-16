balls = int(input('How many ping pong balls can you hold in your hand? '))
hands = int(input('How many hands do you have? '))
if hands == 1:
  print('You can hold ' + balls + ' balls in your hand!')
else:
  print('You can hold ' + (balls * hands) + ' balls in your hands!')

