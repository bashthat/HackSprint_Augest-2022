namespace Namespace {
    
    using pygame;
    
    using sys;
    
    using random;
    
    using Vector2 = pygame.math.Vector2;
    
    using System.Collections.Generic;
    
    using System;
    
    public static class Module {
        
        static Module() {
            @"
creating the snake game
";
            pygame.init();
            pygame.time.set_timer(UPDATE_SCREEN, 150);
            pygame.quit();
            sys.exit();
            Game.update();
            snake.body_moves();
            snake.direction = Vector2(0, -1);
            snake.direction = Vector2(0, 1);
            snake.direction = Vector2(-1, 0);
            snake.direction = Vector2(1, 0);
            screen.fill((170, 25, 200));
            fruit.draw_fruit();
            snake.draw();
            Game.draw();
            pygame.display.update();
            clock.tick(60);
        }
        
        public class Snake {
            
            public Snake() {
                this.body = new List<object> {
                    Vector2(0, 0),
                    Vector2(6, 10),
                    Vector2(7, 10)
                };
                this.direction = Vector2(1, 0);
                this.new_block = false;
            }
            
            public virtual object draw() {
                foreach (var blx in this.body) {
                    var x_pos = Convert.ToInt32(blx.x * cell_size);
                    var y_pos = Convert.ToInt32(blx.y * cell_size);
                    var x_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size);
                    pygame.draw.rect(screen, (183, 191, 122), x_rect);
                }
            }
            
            public virtual object move() {
                object body_copy;
                if (this.new_length) {
                    body_copy = this.body[:: - 1];
                    body_copy.insert(0, body_copy[0] + this.direction);
                    this.body = body_copy;
                    this.new_length = false;
                } else {
                    body_copy = this.body[:: - 1];
                    body_copy.insert(0, body_copy[0] + this.direction);
                    this.body = body_copy;
                }
            }
            
            public virtual object add_length() {
                this.new_block = true;
            }
        }
        
        public class FRUIT {
            
            public FRUIT() {
                this.random_fruit();
            }
            
            public virtual object spawn_fruit() {
                var fruit_obj = pygame.Rect(Convert.ToInt32(this.pos.x * cell_size, this.pos.y * cell_size, cell_size, cell_size));
                pygame.draw.rect(screen, (255, 116, 155), fruit_obj);
            }
            
            public virtual object random_fruit() {
                this.x = random.randint(0, cell_num - 1);
                this.y = random.randint(0, cell_num - 1);
                this.position = Vector2(this.x, this.y);
            }
            
            public virtual object move_snake() {
                var body_moves = this.body[:: - 1];
                body_moves.insert(0, this.body[0] + this.direction);
                this.body = body_moves[":"];
            }
        }
        
        public class Game {
            
            public Game() {
                this.snake = Snake();
                this.fruit = FRUIT();
            }
            
            public virtual object update() {
                this.snake.move_snake[0];
                this.handle_events();
            }
            
            public virtual object draw() {
                this.snake.draw();
                this.fruit.spawn_fruit();
            }
            
            public virtual object handle_events() {
                if (this.fruit.pos == this.snake.body[0]) {
                    this.fruit.random_fruit();
                    this.snake.body.append(this.snake.body[-1] + this.snake.direction);
                    Console.WriteLine("fruit!");
                }
            }
        }
        
        public static object cell_size = 40;
        
        public static object cell_num = 20;
        
        public static object screen = pygame.display.set_mode((cell_num * cell_size, cell_num * cell_size));
        
        public static object clock = pygame.time.Clock();
        
        public static object fruit = FRUIT();
        
        public static object snake = Snake();
        
        public static object UPDATE_SCREEN = pygame.USEREVENT;
    }
}