# Exercise 04 – Async Queue Processor

**Goal:**  
Practice Python's `async` / `await`, batching, and concurrency. This simulates
a simple queue processing service (similar to Azure Queue / Service Bus).

Here are some useful Python docs to reference while working on it.

---

## 🔗 Useful Python Documentation

### 🧵 Async & Concurrency

- `asyncio` (main async framework) → https://docs.python.org/3/library/asyncio.html
- Coroutines & `async` / `await` → https://docs.python.org/3/reference/expressions.html#await
- `asyncio.gather` → https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
- Running async programs with `asyncio.run()` → https://docs.python.org/3/library/asyncio-runner.html#asyncio.run

### 🧱 Types & Protocols

- `dataclasses` → https://docs.python.org/3/library/dataclasses.html
- `typing.Protocol` → https://docs.python.org/3/library/typing.html#typing.Protocol
- Type hints in general → https://docs.python.org/3/library/typing.html

### 🧾 General Python

- Functions & `def` → https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Exceptions → https://docs.python.org/3/tutorial/errors.html

---

## Files

- `starter_queue_processor.py` – starter with TODOs
- `solution_queue_processor.py` – reference solution

---

## Scenario

We have:

- `InMemoryQueue` – a basic in-memory queue
- `process_queue_forever` – an async loop that:
  - Receives batches of messages
  - Processes them with a handler
  - Waits when there are no messages

Core building blocks in the starter:

- `MessageHandler` – a `Protocol` describing any async callable that takes a `str`.
- `InMemoryQueue.receive_batch` – simulates an async network call with `asyncio.sleep`.
- `process_queue_forever` – uses `await` and `asyncio.gather` for concurrency.

---

## Your Tasks

### 1️⃣ Implement `InMemoryQueue.receive_batch(self, batch_size: int) -> list[str]`

In this method:

- Take **up to** `batch_size` messages from `self.messages`.
- Remove those messages from the list (like popping from a real queue).
- Return the batch as a `list[str]`.

Hints:

- Use slicing to take the first `batch_size` items
- Use `del` or reassign the list to remove the items you just took
- Remember: the method is `async`, so it already simulates I/O using `await asyncio.sleep(0.1)`

Docs:

- Lists & slicing → https://docs.python.org/3/tutorial/introduction.html#lists

---

### 2️⃣ Implement the body of `process_queue_forever`

Signature:

```python
async def process_queue_forever(
    queue: InMemoryQueue,
    handler: MessageHandler,
    batch_size: int = 5,
    poll_interval_seconds: float = 1.0,
) -> None:
```

Behavior:

1. Run in an **infinite loop** until cancelled.
2. In each iteration:
   - `batch = await queue.receive_batch(batch_size)`
   - If `batch` is empty:
     - `await asyncio.sleep(poll_interval_seconds)`
     - `continue`
   - If `batch` has messages:
     - Call the handler on each message **concurrently** using `asyncio.gather`:
       ```python
       await asyncio.gather(*(handler(msg) for msg in batch))
       ```
3. Catch `asyncio.CancelledError` and allow graceful shutdown.

Docs:

- `while True:` loops → basic control flow
- `asyncio.gather` → https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
- Task cancellation → https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel

---

### 3️⃣ Run the script

The starter includes a `main()` similar to:

```python
async def main() -> None:
    queue = InMemoryQueue(messages=[f"msg-{i}" for i in range(10)])
    task = asyncio.create_task(process_queue_forever(queue, example_handler))

    await asyncio.sleep(5)
    task.cancel()
    await task
```

And the usual entrypoint:

```python
if __name__ == "__main__":
    asyncio.run(main())
```

Steps:

1. Run the script.
2. Watch messages being processed (`Processed: msg-0`, etc.).
3. Observe that after a few seconds, the main task cancels the background processor gracefully.

Docs:

- `asyncio.create_task` → https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task
- `asyncio.sleep` → https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep

---

## Discussion Points

- How does Python `async`/`await` compare to C# async?
- Why use `asyncio.gather` instead of processing messages sequentially?
- How might this map to processing messages from:
  - Azure Queue Storage
  - Azure Service Bus
  - AWS SQS, etc.

Consider:

- Backpressure: what happens if messages arrive faster than you process them?
- Error handling in handlers: what if one message fails? Do you fail the whole batch?

---

## Stretch Goals

- Add a **max number of messages** to process before stopping (e.g. stop after 100 messages).
- Add simple metrics:
  - Total messages processed
  - Average processing time per message
- Add basic logging instead of `print`, using the `logging` module:
  - Docs → https://docs.python.org/3/library/logging.html

---

By completing this exercise, you will:

- Deepen your understanding of Python `async` / `await`
- Learn to batch and process work concurrently
- Practice designing clean async APIs that are easy to plug into real queue systems
