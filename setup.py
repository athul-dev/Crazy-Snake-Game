import cx_Freeze

executables = [cx_Freeze.Executable("snake-version1.py")]

cx_Freeze.setup(

    name ="Snakeey",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","brick.png","brick-1.jpg","brick-2.jpg","brick-3.jpg","flute.mp3","mongoose.png","snake.png","snake-icon.png"]}},
    description = "Mottuma's Snake Game",
    executables = executables
)
