# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import text_generator_pb2 as text__generator__pb2


class TextGeneratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/TextGenerator/Generate',
                request_serializer=text__generator__pb2.GenerateRequest.SerializeToString,
                response_deserializer=text__generator__pb2.GenerateResponse.FromString,
                )
        self.GenerateStreamed = channel.unary_stream(
                '/TextGenerator/GenerateStreamed',
                request_serializer=text__generator__pb2.GenerateStreamedRequest.SerializeToString,
                response_deserializer=text__generator__pb2.GenerateStreamedResponse.FromString,
                )


class TextGeneratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Generate text and return result.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateStreamed(self, request, context):
        """Generate text and stream intermediate result. The last response should be treated as a completed response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextGeneratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=text__generator__pb2.GenerateRequest.FromString,
                    response_serializer=text__generator__pb2.GenerateResponse.SerializeToString,
            ),
            'GenerateStreamed': grpc.unary_stream_rpc_method_handler(
                    servicer.GenerateStreamed,
                    request_deserializer=text__generator__pb2.GenerateStreamedRequest.FromString,
                    response_serializer=text__generator__pb2.GenerateStreamedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextGenerator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextGenerator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextGenerator/Generate',
            text__generator__pb2.GenerateRequest.SerializeToString,
            text__generator__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateStreamed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TextGenerator/GenerateStreamed',
            text__generator__pb2.GenerateStreamedRequest.SerializeToString,
            text__generator__pb2.GenerateStreamedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
