import asyncio
import  time

def sync_function(test_param: str) -> str:
    print("This is a synchronous function.")
    time.sleep(2)  # Simulate a blocking operation
    return f"Synchronous result: {test_param}"

async def async_function(test_param: str) -> str:
    print("This is an asynchronous function.")
    await asyncio.sleep(2)  # Simulate a non-blocking operation
    return f"Asynchronous result: {test_param}"

async def main():
    start_time = time.time()
    print(f"Starting execution at {time.strftime('%H:%M:%S', time.localtime(start_time))}")
    
    # SYNC FUNCTION
    sync_result = sync_function("Hello, Sync!")
    print(sync_result)

    # FUTURE 
    loop = asyncio.get_running_loop()
    future = loop.create_future() # A promise-like object
    print(f"Empty future: {future}")
    future.set_result("Future is done!")
    future_result = await future
    print(f"Future result: {future_result}")

    # COROUTINE #
    coroutine_obj = async_function("Hello, Coroutine!")
    print(f"Coroutine object: {coroutine_obj}")
    coroutine_result = await coroutine_obj
    print(f"Coroutine result: {coroutine_result}")

    # TASK
    task = asyncio.create_task(async_function("Hello, Task!"))
    print(f"Task object: {task}")
    task_result = await task
    print(f"Task result: {task_result}")
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nExecution completed at {time.strftime('%H:%M:%S', time.localtime(end_time))}")
    print(f"Total time taken: {total_time:.2f} seconds")



if __name__ == "__main__":
    asyncio.run(main()) # Event loop to run the async main function