from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player
if __name__ == "__main__":
    # Test against each bot
    print("Testing against Quincy")
    play(player, quincy, 1000, verbose=True)
    
    print("Testing against Abbey")
    play(player, abbey, 1000, verbose=True)
    
    print("Testing against Kris")
    play(player, kris, 1000, verbose=True)
    
    print("Testing against Mrugesh")
    play(player, mrugesh, 1000, verbose=True)

    # Run unit tests
    # Uncomment the line below to run the unit tests
    # import test_module; test_module.main()
