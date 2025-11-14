from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Protocol, Any, Iterable


class MessageHandler(Protocol):
    """
    Protocol for message handling.

    Any async callable with this signature can be used
    (similar to an interface in C#).
    """

    async def __call__(self, message: str) -> None:
        ...


@dataclass
class InMemoryQueue:
    """Very small in-memory queue to simulate queue processing."""
    messages: list[str]

    async def receive_batch(self, batch_size: int) -> list[str]:
        """
        Pop up to batch_size messages from the queue.

        TODO:
          - Take up to batch_size items from self.messages.
          - Remove them from the list.
          - Return them.

        NOTE: We simulate network I/O with asyncio.sleep.
        """
        # Simulate network delay
        await asyncio.sleep(0.1)

        # TODO: implement
        raise NotImplementedError("receive_batch is not implemented yet")


async def process_queue_forever(
    queue: InMemoryQueue,
    handler: MessageHandler,
    batch_size: int = 5,
    poll_interval_seconds: float = 1.0,
) -> None:
    """
    Continuously:
      - Fetch a batch of messages.
      - Process each message using the handler.
      - Wait poll_interval_seconds when there are no messages.

    TODO:
      - Implement loop that only exits on CancelledError.
      - Use asyncio.gather to process a batch concurrently.
    """
    try:
        while True:
            batch = await queue.receive_batch(batch_size)
            if not batch:
                await asyncio.sleep(poll_interval_seconds)
                continue

            # TODO: process each message concurrently with handler
            raise NotImplementedError("process_queue_forever body is not implemented yet")
    except asyncio.CancelledError:
        # allow graceful shutdown
        return


async def example_handler(message: str) -> None:
    """Simple message handler for demo purposes."""
    await asyncio.sleep(0.2)
    print(f"Processed: {message}")


async def main() -> None:
    """
    Manual test:
      - Creates a queue with 10 messages.
      - Starts processing in the background.
      - Cancels after a few seconds.
    """
    queue = InMemoryQueue(messages=[f"msg-{i}" for i in range(10)])
    task = asyncio.create_task(process_queue_forever(queue, example_handler))

    await asyncio.sleep(5)
    task.cancel()
    await task


if __name__ == "__main__":
    asyncio.run(main())
