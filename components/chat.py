import arcade, arcade.gui

# how many message will be store in chat_list and show on the screen
CHAT_LIST_SIZE = 10

window = None

def send_message(message):
    pass

class ChatInputBox(arcade.gui.UIInputBox):
    """ Entry field for messages to be sent """
    def __init__(self, window):
        super().__init__()
        self.alpha = 0
        self.id = 'chat'
        window_size = window.get_size()
        self.width= window_size[0] * .99
        self.height = 25
        self.center_x= window_size[0] / 2
        self.center_y= self.height / 2 + window_size[0] * .005
        self.set_style_attrs(
            font_size = 12,
            font_color = arcade.csscolor.WHITE,
            font_color_hover = arcade.csscolor.WHITE,
            font_color_focus = arcade.csscolor.WHITE,
            bg_color = arcade.csscolor.BLACK,
            border_width = 1,
            border_color = arcade.csscolor.WHITE,
            border_color_hover = arcade.csscolor.WHITE,
            border_color_focus = arcade.csscolor.WHITE,
            bg_color_hover = arcade.csscolor.BLACK,
            bg_color_focus = arcade.csscolor.BLACK,
            margin_left = 5
        )

class UIChat(arcade.gui.UIManager):
    """ Main component for chat, all elements are kept in it, like text input field and messages """
    def __init__(self, window):
        super().__init__()
        self.window_size = window.get_size()
        # crate input field for massage to send
        self.chat_input = ChatInputBox(window)
        # add chat_input to ui_elements
        self.add_ui_element(self.chat_input)
        # list of messages to show
        self.message_list = []
        self.message_alpha = 255

    def store_message(self, message):
        """ store message in message_list """
        # if message_list is this same size like CHAT_LIST_SIZE remove from it the oldest message
        if len(self.message_list) == CHAT_LIST_SIZE:
            self.message_list.pop(0)
        # add message to list
        self.message_list.append(self.chat_input.text)

    def on_key_press(self, symbol: int, modifiers: int):
        # if you press 'T' change visiblity of chat box
        if not self.chat_input.focused:
            if symbol == arcade.key.T:
                # if chat_input is invisible make it visible
                if self.chat_input.alpha == 0:
                    self.chat_input.alpha = 255
                # if chat_input is visible make it invisible
                elif self.chat_input.alpha == 255:
                    self.chat_input.alpha = 0
        # send message if press enter and chat_input is no emty
        if self.chat_input.focused and self.chat_input.text != '':
            if symbol == arcade.key.ENTER:
                send_message(self.chat_input.text)
                self.chat_input.text = ''

    def on_draw(self):
        super().on_draw()
        # draw chat messages
        pos_y = self.window_size[1] -19
        for message in self.message_list:
            arcade.draw_text(
                text = message,
                start_x = 5,
                start_y = pos_y,
                color = arcade.csscolor.WHITE,
            )
            pos_y -= 13

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_chat = UIChat(window)
        
    def update(self, delta_time: float):
        pass
    def on_draw(self):
        arcade.start_render()

def main():
    global window
    window = arcade.Window()
    view = Game()
    window.show_view(view)
    arcade.run()
if __name__ == '__main__':
    main()