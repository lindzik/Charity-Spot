import { Field, ID, ObjectType } from '@nestjs/graphql';

@ObjectType()
export class itemRequestEntity {
    @Field({ nullable: true })
    ID: string
}