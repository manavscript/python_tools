import asyncio
import time

# Key Takeaways:
# Link 1: Socratica
# Link 2: https://www.youtube.com/watch?v=t5Bo1Je9EmE&ab_channel=TechWithTim
# 1: async function decorator
# 2: await which tells where to yield the function control
# 3: gather: to tell where to gather the asynchronous coroutines
# 4: use async.io sleep to figure out when and how much to sleep by
# 5: create_task: we can create some task -> let us see how to do that

# async keyword
# await function which is put in front of waitable functions


async def brewCoffee():
    print("Start brew")
    await asyncio.sleep(3)
    print("end brew")
    return "Coffee Ready"


async def toastBagel():
    print("start toasting bagel")
    await asyncio.sleep(2)
    print("end toasting bagel")
    return "bagel toasted"

# main has become coroutine, has to called slightly different


async def fetch_data():
    print("starting to fetch data")
    await asyncio.sleep(2)
    return {"data": 1}


async def print_numbers():
    for i in range(20):
        print(i)
        await asyncio.sleep(0.1)


async def main():
    start_time = time.time()

    # can batch the subroutines which will be waiting
    batch = asyncio.gather(brewCoffee(), toastBagel())
    result_coffee, result_bagel = await batch

    # result_coffee = brewCoffee()
    # result_bagel = toastBagel()

    print(result_coffee, result_bagel)

    end_time = time.time()
    print(end_time - start_time)

    t1 = asyncio.create_task(fetch_data())
    t2 = asyncio.create_task(print_numbers())

    v_t1 = await t1  # we need await as we did not wait for tasks to finish, we did not get values and things like that
    await t2
    print(v_t1)


if __name__ == "__main__":
    asyncio.run(main())
