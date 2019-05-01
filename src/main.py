from neochi.core.dataflow.data import clap_detector
from neochi.core.dataflow.notifications import clap_detector as CD
import sys
import alsaaudio, time, audioop
import threading
import clapdetector as cld
import redis

def clap_detected_callback(value):
    print('Clap Detected')

def push_to_redis(redis_handler):
    clap_detected = CD.DetectedClap(redis_handler)
    #For test
    #clap_detected.subscribe(clap_detected_callback)
    clap_detected.notify()
    #For test
    #clap_detected.unsubscribe()

clap_detector = cld.ClapDetector("default:CARD=Device")
r = redis.StrictRedis('127.0.0.1', 6379, db=0)
clap_detector.set_on_detect_func(push_to_redis, r)
clap_detector.detect()
