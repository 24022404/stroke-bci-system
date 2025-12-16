import pygame
from pygame.locals import *
import random

# Khởi tạo pygame
pygame.init()

# Cấu hình màn hình
width = 500
height = 600 # Tăng chiều cao một chút để hiển thị HUD
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('BCI Motor Imagery - Rehabilitation Game')

# Màu sắc
GRAY = (100, 100, 100)
GREEN = (76, 208, 56)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 232, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
DARK_BLUE = (10, 10, 50)

# Cấu hình đường đua
road_width = 300
marker_width = 10
marker_height = 50

# Tọa độ các làn đường (Left - Center - Right)
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Biên đường
road_x = 100
road_rect = (road_x, 0, road_width, height)
left_edge_marker = (road_x - 5, 0, marker_width, height)
right_edge_marker = (road_x + road_width - 5, 0, marker_width, height)

# Animation vạch kẻ đường
lane_marker_move_y = 0

# Tọa độ người chơi
player_x = 250
player_y = 450

# Cài đặt khung hình
clock = pygame.time.Clock()
fps = 60

# Trạng thái game
gameover = False
speed = 3
score = 0
confidence_score = 0.85 # Giả lập độ tập trung ban đầu (85%)

# Class Xe (Dùng chung cho cả Player và Enemy)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, is_player=False):
        pygame.sprite.Sprite.__init__(self)
        
        # Vẽ xe bằng hình khối thay vì load ảnh
        width = 30 # Motor nhỏ hơn car (45 -> 30)
        height = 70 # Ngắn hơn xíu (90 -> 70)
        self.image = pygame.Surface([width, height])
        # self.image.fill(color) # Không fill màu nền vội để vẽ chi tiết
        self.image.set_colorkey((0,0,0)) # Làm cho nền đen trong suốt
        
        if is_player:
            # Vẽ Motor của người chơi
            # Thân xe
            pygame.draw.rect(self.image, color, (5, 20, 20, 40)) 
            # Tay lái
            pygame.draw.line(self.image, (200, 200, 200), (0, 25), (30, 25), 4)
            # Đầu người (Mũ bảo hiểm)
            pygame.draw.circle(self.image, (255, 255, 0), (15, 35), 10)
            # Bánh xe (trước/sau)
            pygame.draw.rect(self.image, (50, 50, 50), (10, 5, 10, 15))
            pygame.draw.rect(self.image, (50, 50, 50), (10, 60, 10, 10))
        else:
            # Xe địch (Vẫn là ô tô cho dễ phân biệt hoặc motor khác màu)
            self.image.fill(color)
            pygame.draw.rect(self.image, (0,0,0), (5, 10, width-10, 15)) # Kính
            pygame.draw.rect(self.image, (255, 0, 0), (2, height-5, 8, 4)) # Đèn hậu
            pygame.draw.rect(self.image, (255, 0, 0), (width-10, height-5, 8, 4))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Tạo nhóm Sprites
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Tạo xe người chơi (Màu Đỏ)
player = Vehicle(RED, player_x, player_y, is_player=True)
player_group.add(player)

# Hàm vẽ giao diện BCI (HUD)
def draw_bci_hud(screen, score, confidence):
    # Vẽ nền panel trên cùng
    pygame.draw.rect(screen, DARK_BLUE, (0, 0, width, 80))
    
    font = pygame.font.SysFont('Arial', 18, bold=True)
    
    # 1. Điểm số
    score_text = font.render(f'SCORE: {score}', True, WHITE)
    screen.blit(score_text, (20, 20))
    
    # 2. Thanh Confidence (Quan trọng cho báo cáo)
    conf_label = font.render('BRAIN FOCUS:', True, WHITE)
    screen.blit(conf_label, (20, 50))
    
    # Vẽ thanh bar
    bar_width = 150
    bar_height = 20
    bar_x = 140
    bar_y = 50
    
    # Khung
    pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
    # Phần fill (Màu thay đổi theo độ mạnh)
    fill_width = int(bar_width * confidence)
    color = GREEN if confidence > 0.7 else YELLOW if confidence > 0.4 else RED
    pygame.draw.rect(screen, color, (bar_x + 2, bar_y + 2, fill_width - 4, bar_height - 4))
    
    # Số %
    perc_text = font.render(f'{int(confidence*100)}%', True, color)
    screen.blit(perc_text, (bar_x + bar_width + 10, 50))

    # 3. Trạng thái phân loại
    intent_text = font.render('INTENT:', True, WHITE)
    screen.blit(intent_text, (350, 20))
    
    # Giả lập hiển thị hướng đang nghĩ
    # Nếu xe đang ở làn trái -> Left, Phải -> Right
    current_intent = "CENTER"
    if player.rect.center[0] < center_lane - 10: current_intent = "LEFT"
    elif player.rect.center[0] > center_lane + 10: current_intent = "RIGHT"
    
    intent_val = font.render(current_intent, True, GREEN)
    screen.blit(intent_val, (350, 50))


# Vòng lặp chính
running = True
# Chạy demo tự động (Auto-play) trong 2 giây để chụp ảnh màn hình, sau đó tắt
# Để người dùng chơi thật thì set auto_close = False
auto_close = False 
start_time = pygame.time.get_ticks()

while running:
    
    clock.tick(fps)
    
    # Sự kiện bàn phím
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
                confidence_score = min(1.0, confidence_score + 0.05) # Tăng độ tập trung khi điều khiển đúng
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
                confidence_score = min(1.0, confidence_score + 0.05)
    
    # -- Logic Game --
    if not gameover:
        # Di chuyển vạch kẻ đường
        lane_marker_move_y += speed * 2
        if lane_marker_move_y >= marker_height * 2:
            lane_marker_move_y = 0
            
        # Sinh xe địch ngẫu nhiên
        if len(vehicle_group) < 2:
            add_vehicle = True
            for vehicle in vehicle_group:
                if vehicle.rect.top < vehicle.rect.height * 1.5:
                    add_vehicle = False
                    
            if add_vehicle:
                lane = random.choice(lanes)
                enemy_color = random.choice([BLUE, YELLOW, (255, 100, 0)])
                vehicle = Vehicle(enemy_color, lane, -100) # Xuất hiện từ trên cao
                vehicle_group.add(vehicle)
                
        # Di chuyển xe địch
        for vehicle in vehicle_group:
            vehicle.rect.y += speed
            if vehicle.rect.top >= height:
                vehicle.kill()
                score += 1
                # Giả lập độ tập trung dao động ngẫu nhiên
                confidence_score = max(0.4, min(1.0, confidence_score + random.uniform(-0.1, 0.1)))
                
                if score > 0 and score % 5 == 0:
                    speed += 1

        # Va chạm
        if pygame.sprite.spritecollide(player, vehicle_group, False):
            gameover = True
            confidence_score = 0.2 # Va chạm -> Mất tập trung

    # -- VẼ HÌNH --
    # 1. Vẽ cỏ (Nền)
    screen.fill(GREEN)
    
    # 2. Vẽ đường
    pygame.draw.rect(screen, GRAY, road_rect)
    
    # 3. Vẽ vạch kẻ đường
    pygame.draw.rect(screen, YELLOW, left_edge_marker)
    pygame.draw.rect(screen, YELLOW, right_edge_marker)
    
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, WHITE, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, WHITE, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
    # 4. Vẽ xe
    player_group.draw(screen)
    vehicle_group.draw(screen)
    
    # 5. Vẽ HUD BCI
    draw_bci_hud(screen, score, confidence_score)
    
    # 6. Game Over
    if gameover:
        pygame.draw.rect(screen, RED, (0, 250, width, 100))
        font = pygame.font.SysFont('Arial', 30, bold=True)
        text = font.render('GAME OVER', True, WHITE)
        text_rect = text.get_rect(center=(width/2, 300))
        screen.blit(text, text_rect)
        
    pygame.display.update()

    # Tự động lưu ảnh sau 1 giây (khoảng 60 frames) để người dùng có ảnh báo cáo ngay
    # if pygame.time.get_ticks() - start_time > 1000 and pygame.time.get_ticks() - start_time < 1100:
    #      pygame.image.save(screen, "bci_car_game_screenshot.png")
    #      print("Đã chụp ảnh màn hình game: bci_car_game_screenshot.png")
         
    # Tự động thoát sau 3 giây để không treo terminal
    if auto_close and pygame.time.get_ticks() - start_time > 3000:
        running = False

pygame.quit()

