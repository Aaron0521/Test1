""""""

from logcenter.logger.loggers import loggerHander
import time
import multiprocessing


def run(que):
    log = loggerHander(queue=que)
    a = 0
    while True:
        log.info(hospital_id=f'xx医院{a}', case_id='45111', task='试一下', status='不晓得', error='还没有', desc='说啥呢', count='10',
                 ext1='', ext2='')
        time.sleep(0.2)
        a += 1


def get_mul(que):
    logs = loggerHander(queue=que)
    logs.listen()


if __name__ == '__main__':
    my_que = multiprocessing.Queue()
    p2 = multiprocessing.Process(target=get_mul, args=(my_que,))
    p2.start()
    run(my_que)


