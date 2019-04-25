from requests import Session
from signalr import Connection
import json
import gevent
from gevent import monkey
import requests


def signalRTest():
    # monkey.patch_all()
    # from requests.packages.urllib3.util.ssl_ import create_urllib3_context
    # create_urllib3_context()
    with Session() as session:
        # create a connection
        # connection = Connection("http://tvbetapi.net/mainfeed", session)
        # connection = Connection("http://192.168.212.172:11009/mainfeed", session)
        # connection = Connection("http://192.168.212.172:9005/mainfeed", session)
        # connection = Connection("http://localhost:11009/mainfeed", session)
        # connection = Connection("http://localhost:30258/mainfeed", session)
        # connection = Connection("http://localhost:30258/feedhub", session)
        # connection = Connection("http://localhost:14507/hubs", session)
        # connection = Connection("http://localhost:44312/hubs", session)
        # connection = Connection("http://192.168.212.172:11011/hubs", session)
        connection = Connection("http://192.168.212.172:11993/hubs", session)
        # connection = Connection("http://192.168.212.172:9005/feedhub", session)
        # get chat hub
        # feedHub = connection.register_hub('mainfeed')
        feedHub = connection.register_hub('FeedHub')

        # start a connection
        connection.start()

        # create new chat message handler
        def print_received_message(data):
            t = json.dumps(data)
            temp = json.loads(t)
            print(temp)
            # if temp['NI'] != 1:
            #     print(temp)

            # if temp['NI'] == 8:
            #     print('LastHands: ', temp['D']['LH'])
            #     print('Hands: ', temp['D']['H'])
            #     print('------')
        # create error handler
        def print_error(error):
            print('error: ', error)

        # receive new chat messages from the hub
        # feedHub.client.on('addMessage', print_received_message)
        # feedHub.client.on('addMessage', print_received_message)
        feedHub.client.on('TimingSubscribe', print_received_message)
        feedHub.client.on('VideoGamesSubscribe', print_received_message)
        feedHub.client.on('GamesInfoSubscribe', print_received_message)
        feedHub.client.on('GamesSubscribe', print_received_message)
        feedHub.client.on('GamesLastResultsSubscribe', print_received_message)
        feedHub.client.on('GamesStatisticsSubscribe', print_received_message)
        feedHub.client.on('GamesEventsSubscribe', print_received_message)
        feedHub.client.on('PromterGameSubscribe', print_received_message)
        #
        # change chat topic
        # chat.client.on('topicChanged', print_topic)

        # process errors
        connection.error += print_error
        money = 10
        # start connection, optionally can be connection.start()
        with connection:
            # post new message
            # feedHub.server.invoke('send', '{"M":14,"GT":5}')
            # SubscribeOnGame
            # feedHub.server.invoke('send', '{"M":2,"GT":4,"C":"EUR","CID":46,"CG":5,"L":"en"}')
            # feedHub.server.invoke('send', '{"M":3,"GT":3,"C":"EUR","CI":127,"CG":3,"L":"en"}')
            # SubOnGame
            # feedHub.server.invoke('send', '{"M":16,"GID":90018722430,"CID":35,"L":"en"}')
            # feedHub.server.invoke('send', '{"M":17,"CI":192,"GID":30001947193,"GT":3,"L":"ru"}')
            # feedHub.server.invoke('send', '{"M":20,"GID":50007287757,"GT":5}')
            # SubscribeOnGameStatistic
            feedHub.server.invoke('SubscribeOnTiming', [2])
            # feedHub.server.invoke('SubscribeOnVideoGames', [2], 2026)
            # feedHub.server.invoke('SubscribeOnGamesInfo', 2, 3)
            # feedHub.server.invoke('SubscribeOnPromterGame', 5)
            # feedHub.server.invoke('SubscribeOnGamesLastResults', 2, 3)
            # feedHub.server.invoke('SubscribeOnGamesStatistics', 6)
            # feedHub.server.invoke('SubscribeOnGames', [{"i": 6703045, "t": 5}], 46)
            # feedHub.server.invoke('SubscribeOnCashDeskGames', [{"i": 90000037378, "t": 2}], 127)
            # feedHub.server.invoke('SubscribeOnCashDeskGamesEvents', [{"i": 131197, "t": 7, "e": [{"t": 123, "p": ["175.5"]}, {"t": 2169, "p": ["-1", "0"]}]}], 127, 0)
            # SubscribeOnPromterGame
            # feedHub.server.invoke('send', '{"M":21,"GT":2,"CI":121,"CE":15,"EM":2,"EI":[{"ET":21,"P":[1]},{"ET":4043,"P":[1,2,3,4,5,6]},{"ET":23,"P":[18.5]},{"ET":30,"P":[]}]}')
            # feedHub.server.invoke('send', '{"M": 21,"GT": 2,"CI":121,"CE":30,"EM":1,"EI":[{"ET":21,"P":["1"]}]}')
            # feedHub.server.invoke('send', '{"M":8,"GT":3}')
            # feedHub.server.invoke('send', '{"M":9,"CID":46}')
            # feedHub.server.invoke('send', '{"GTS":[2],"C":"EUR","L":"en","PM":0.05,"M":19}')
            # feedHub.server.invoke('send', '{"M":4,"GT":2,"CG":2}')

            # change chat topic
            # chat.server.invoke('setTopic', 'Welcome python!')

            # invoke server method that throws error
            # chat.server.invoke('requestError')

            # chat.server.invoke('send', 'Bye-bye!')

            # wait a second before exit
            connection.wait(None)


if __name__ == "__main__":
    signalRTest()
